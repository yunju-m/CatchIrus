import json
from django.http import JsonResponse
from django.core import serializers

from . import models
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import FileSave, RankFile, UserFile
from .forms import FileSaveForm, UserFileForm
from django.core.paginator import Paginator 
from django.utils import timezone

def home(request):
    # 제출버튼을 클릭하면 POST 수행
    if request.method == 'POST':
        # 1. FileSave 모델에 업로드 파일 저장
        file_upload = request.FILES["input-file"]
        filename = request.FILES["input-file"].name
        filesize = request.FILES["input-file"].size
        filesave = FileSave(
            filename = filename,
            file_upload = file_upload,
            filesize = filesize,
        )
        filesave.save()

        # 2. UserFile 모델에 로그인 여부에 따라 사용자, 파일, 날짜 저장
        # 로그인 o => 닉네임 / 로그인 x => AnonymousUser => visitor(방문객)
        date = timezone.now()
        
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            userfile = UserFile(
                author = user,
                authorname = user.username,
                filename = filename,
                date = date,
            )
        else:
            userfile = UserFile(
                authorname = 'visitor',
                filename = filename,
                date = date,
            )

        userfile.save()

        # 3. RankFile 모델에 전체 업로드 파일과 조회수 정보 저장
        if is_filename_in_RankFile(filesave.filename):
            rankfile = RankFile.objects.get(filename=filesave.filename)
            rankfile.count += 1
        else:
            rankfile = RankFile(
                filename=filesave.filename,
                count = 1
            )
        rankfile.save()

        return redirect('file')
    
    # 홈페이지를 불러오면(GET) form생성하고 home.html 화면 출력
    else:
        # 기존 파일과 임시 방문객 정보 초기화하고 새롭게 업로드한 정보만 전달
        models.FileSave.objects.all().delete()
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
    return RankFile.objects.filter(filename=filename).exists() 

# /file 매핑되면 실행   
def fileupload(request):
    # 로그인, 비로그인 사용자 구분하여 정보 추출 -> usermodel 저장
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        usermodel = models.UserFile.objects.filter(authorname=user).order_by('-date')
    else:
        usermodel = models.UserFile.objects.filter(authorname='visitor').order_by('-date')
    
    # 업로드 파일과 동일한 userfile의 정보를 추출
    file_objects = models.FileSave.objects.all()
    for file_object in file_objects:
        upload_filename = file_object.filename
    matchfilemodel = models.UserFile.objects.filter(filename=upload_filename).order_by('-date')

    page = request.GET.get('page', '1') # 페이지(1페이지부터 생성)
    paginator = Paginator(usermodel, 10)    # 페이지당 10개씩
    userpage_obj = paginator.get_page(page)
    paginator = Paginator(matchfilemodel, 10)
    matchpage_obj = paginator.get_page(page)

    filemodel = models.FileSave.objects.all()   # 업로드된 파일 정보
    rankmodel = models.RankFile.objects.all().order_by('-count')   # 파일별 이름, 횟수 정보 (조회수 많은 순서부터 출력)

    if request.method == "POST":
        # usermodel --> Json 변환
        usermodeljson = serializers.serialize('json',usermodel)
        matchfilemodeljson = serializers.serialize('json', matchfilemodel)
        
        return JsonResponse({'usermodel': usermodeljson, 'userpage': userpage_obj.number, 'matchmodel': matchfilemodeljson, 'matchpage': matchpage_obj.number})
    else:
        return render(request, 'fileResult.html', {'filemodel': filemodel, 'usermodel': userpage_obj, 'matchfilemodel':matchfilemodel, 'rankmodel': rankmodel})
    
# 모델 결과 값 chart text에 출력하는 함수
def filechart(request):
    predictresultmodel = models.PredictProbability.objects.all()    #모델 결과 정보
    predictresultmodel_json = serializers.serialize('json', predictresultmodel)                      
    predictresultmodel_list = json.loads(predictresultmodel_json)
    proba = [item["fields"]["proba"] for item in predictresultmodel_list]
    result = [item["fields"]["result"] for item in predictresultmodel_list]
    return JsonResponse({'proba':proba, 'result': result})