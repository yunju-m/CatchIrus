import json
from django.http import JsonResponse
from django.core import serializers

from . import models
from django.shortcuts import redirect, render
from .models import FileSave, PredictProbability, RankFile, UserFile
from .forms import FileSaveForm, UserFileForm
from django.core.paginator import Paginator 
from django.utils import timezone
from django.db.models import Count

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

        # # 파일이름별 횟수 출력하여 랭크생성
        user_files = UserFile.objects.values('filename').distinct()
        user_files = UserFile.objects.values('filename').annotate(count=Count('filename'))
        
        for file in user_files:
            if is_filename_in_RankFile(file['filename']):
                rankfile = RankFile.objects.get(filename=file['filename'])
                rankfile.count = file['count']
                rankfile.save()
            else:
                rankfile = RankFile(
                    filename=file['filename'],
                    count = file['count']
                )
                rankfile.save()
                
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
            os.system(f"objdump -d \"./media/home/files/{year}/0{month}/{day}/{name}.exe\" | grep \"^ \" | cut -f 3 | cut -f 1 -d \" \" >> ./home/user_util/temp/{name}.txt")  # opcode
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

        probability = PredictProbability(
            result = pred_result, #Benign or Malware
            proba = result, # 퍼센트
        )
        
        probability.save()
        ''' 선영이 코드 끝 '''

        return redirect('file')
    # 홈페이지를 불러오면 form생성하고 home.html 화면 출력
    else:
        # 방문객과 기존 파일들을 모두 제거하여 새롭게 입력한 값들만 출력
        models.FileSave.objects.all().delete()
        models.PredictProbability.objects.all().delete()
        models.UserFile.objects.filter(author=None).delete()
        filesaveForm = FileSaveForm
        usersaveForm = UserFileForm
        context = {
            'filesaveForm': filesaveForm,
            'usersaveForm': usersaveForm,
        }
        return render(request, 'home.html', context)

# RankFile에 filename이 들어있는지 판단하는 함수
def is_filename_in_RankFile(filename):
    print("응애: ", filename)
    return RankFile.objects.filter(filename=filename).exists() 

# /file 매핑되면 file 정보를 fileResult.html에 출력    
def fileupload(request):
    # user별로 정보 추출
    if request.user.get_username() == '':
        usermodel = models.UserFile.objects.filter(author=None)
    else:
        usermodel = models.UserFile.objects.filter(author=request.user)
    
    # 업로드 파일과 동일한 userfile의 정보를 추출
    file_objects = models.FileSave.objects.all()
    for file_object in file_objects:
        upload_file = file_object.filename
    matchfilemodel = models.UserFile.objects.filter(filename=upload_file)

    page = request.GET.get('page', '1') # 페이지(1페이지부터 생성)
    paginator = Paginator(usermodel, 10)    # 페이지당 10개씩
    userpage_obj = paginator.get_page(page)
    paginator = Paginator(matchfilemodel, 10)
    matchpage_obj = paginator.get_page(page)

    filemodel = models.FileSave.objects.all()   # 업로드된 파일 정보
    rankmodel = models.RankFile.objects.all()   # 파일별 이름, 횟수 정보
    probamodel = models.PredictProbability.objects.all()

    if request.method == "POST":
        # usermodel --> Json 변환
        usermodeljson = serializers.serialize('json',usermodel)
        matchfilemodeljson = serializers.serialize('json', matchfilemodel)
        
        return JsonResponse({'usermodel': usermodeljson, 'userpage': userpage_obj.number, 'matchmodel': matchfilemodeljson, 'matchpage': matchpage_obj.number})
    else:
        return render(request, 'fileResult.html', {'filemodel': filemodel, 'usermodel': userpage_obj, 'matchfilemodel':matchfilemodel, 'rankmodel': rankmodel, 'probamodel': probamodel})
    
# 모델 결과 값 chart text에 출력하는 함수
def filechart(request):
    predictresultmodel = models.PredictProbability.objects.all()    #모델 결과 정보
    predictresultmodel_json = serializers.serialize('json', predictresultmodel)                      
    predictresultmodel_list = json.loads(predictresultmodel_json)
    proba = [item["fields"]["proba"] for item in predictresultmodel_list]
    result = [item["fields"]["result"] for item in predictresultmodel_list]
    return JsonResponse({'proba':proba, 'result': result})