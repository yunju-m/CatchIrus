from django.http import JsonResponse
from django.core import serializers

from . import models
from django.shortcuts import redirect, render
from .models import FileSave, UserFile, PredictProbability
from .forms import FileSaveForm, UserFileForm, PredictProbabilityForm
from django.core.paginator import Paginator 
from django.utils import timezone

# 선영이가 추가한 라이브러리
import joblib
from .user_util.txt_to_csv import Change
from .user_util.data_preprocessing import Data
import os #os.getcwd() -> 현재 디렉토리 확인

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import operator
from sklearn import svm
from sklearn import metrics
import xgboost
from datetime import datetime

def home(request):
    # 제출버튼을 클릭하면 해당 file정보를 저장하고 /file로 매핑
    if request.method == 'POST':
        author = request.user
        date = timezone.now()
        file_upload = request.FILES["input-file"]
        filename = request.FILES["input-file"].name
        filesize = request.FILES["input-file"].size
        filesave = FileSave(
            filename = filename,
            file_upload = file_upload,
            filesize = filesize,
        )
        
        # 로그인 o => 닉네임 / 로그인 x => visitor(방문객)
        if author.get_username() == '':
            UserFile.author = 'visitor'
            userfile = UserFile(
                authorname = 'visitor',
                filename = filename,
                date = date,
            )
        else:
            userfile = UserFile(
                author = author,
                authorname = author,
                filename = filename,
                date = date,
            )
        userfile.save()
        filesave.save()

        ''' 선영이 코드 시작 '''
        # 폴더 생성
        try:
            os.mkdir("./home/user_util/temp")
            os.mkdir("./home/user_util/result")
        except:
            print("파일이 존재합니다.")

        # opcode 추출 txt파일을 csv파일로 변환
        name = os.path.splitext(filename)[0]
        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day
        
        os.system(f"echo {name} > ./home/user_util/temp/{name}.txt")  # 파일 이름
        if(month < 10):
            os.system(f"objdump -d \"./media/home/files/{year}/0{month}/0{day}/{name}.exe\" | grep \"^ \" | cut -f 3 | cut -f 1 -d \" \" >> ./home/user_util/temp/{name}.txt")  # opcode
        else:
            os.system(f"objdump -d \"./media/home/files/{year}/{month}/{day}/{name}.exe\" | grep \"^ \" | cut -f 3 | cut -f 1 -d \" \" >> ./home/user_util/temp/{name}.txt")  # opcode
        
        t_to_c = Change("./home/user_util/temp/", f"{name}")
        t_to_c.txt_to_csv()

        # 4-gram 전처리하여 파일 저장
        result = Data(f"./home/user_util/temp/{name}.csv", f"./home/user_util/result/{name}.csv")
        result.predict()
        
        # 결과 파일 빼고 모두 삭제
        for file in os.scandir("./home/user_util/temp"):
            os.remove(file)

        # 탐지된 결과 출력
        rfc_model = joblib.load('rfc_model_400.pkl')

        data = pd.read_csv(f'./home/user_util/result/{name}.csv')
        data = data.dropna(axis=1)
        data = data.drop(['file name', 'class'], axis=1)

        y_pred = rfc_model.predict(data)
        y_prob = rfc_model.predict_proba(data)
        pred_result = ""
        result = 0

        if(y_pred[0] == 1.):
            pred_result = "Benign"
            result = float(y_prob[0][1])
        elif(y_pred[0] == 0.):
            pred_result = "Malware"
            result = float(y_prob[0][0])

        result = int(round(result, 2) * 100)

        filesave.result = pred_result
        probability = PredictProbability(
            proba = result,
        )
        probability.save()
        filesave.save()
        ''' 선영이 코드 끝 '''

        return redirect('file')
    # 홈페이지를 불러오면 form생성하고 home.html 화면 출력
    else:
        # 방문객과 기존 파일들을 모두 제거하여 새롭게 입력한 값들만 출력
        models.FileSave.objects.all().delete()
        models.UserFile.objects.filter(author=None).delete()
        filesaveForm = FileSaveForm
        usersaveForm = UserFileForm
        predictprobabilityForm = PredictProbabilityForm
        context = {
            'filesaveForm': filesaveForm,
            'usersaveForm': usersaveForm,
            'probabilityForm': predictprobabilityForm
        }
        return render(request, 'home.html', context)

# /file 매핑되면 file 정보를 fileResult.html에 출력    
def fileupload(request):
    page = request.GET.get('page', '1') # 페이지(1페이지부터 생성)
    filemodel = models.FileSave.objects.all()
    if request.user.get_username() == '':
        usermodel = models.UserFile.objects.filter(author=None)
    else:
        usermodel = models.UserFile.objects.filter(author=request.user)
    paginator = Paginator(usermodel, 10)    # 페이지당 10개씩
    userpage_obj = paginator.get_page(page)
    if request.method == "POST":
        print("post 시작이요~~")
        # usermodel --> Json 변환
        usermodeljson = serializers.serialize('json',usermodel)
        return JsonResponse({'usermodel': usermodeljson, 'userpage': userpage_obj.number})
    else:
        return render(request, 'fileResult.html', {'filemodel': filemodel, 'usermodel': userpage_obj})