from django.http import JsonResponse
from django.core import serializers

from . import models
from django.shortcuts import redirect, render
from .models import FileSave, UserFile
from .forms import FileSaveForm, UserFileForm
from django.core.paginator import Paginator 
from django.utils import timezone

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
        return redirect('file')
    # 홈페이지를 불러오면 form생성하고 home.html 화면 출력
    else:
        # 방문객과 기존 파일들을 모두 제거하여 새롭게 입력한 값들만 출력
        models.FileSave.objects.all().delete()
        models.UserFile.objects.filter(author=None).delete()
        filesaveForm = FileSaveForm
        usersaveForm = UserFileForm
        context = {
            'filesaveForm': filesaveForm,
            'usersaveForm': usersaveForm,
        }
        return render(request, 'home.html', context)

# /file 매핑되면 file 정보를 fileResult.html에 출력    
def fileupload(request):
    # user별로 정보 추출
    if request.user.get_username() == '':
        usermodel = models.UserFile.objects.filter(author=None)
    else:
        usermodel = models.UserFile.objects.filter(author=request.user)
    
    # file별로 정보 추출
    file_objects = models.FileSave.objects.all()
    for file_object in file_objects:
        upload_file = file_object.filename
    matchfilemodel = models.UserFile.objects.filter(filename=upload_file)
    
    page = request.GET.get('page', '1') # 페이지(1페이지부터 생성)
    paginator = Paginator(usermodel, 10)    # 페이지당 10개씩
    userpage_obj = paginator.get_page(page)
    filemodel = models.FileSave.objects.all()   # 업로드된 파일 정보
    if request.method == "POST":
        # usermodel --> Json 변환
        usermodeljson = serializers.serialize('json',usermodel)
        return JsonResponse({'usermodel': usermodeljson, 'userpage': userpage_obj.number})
    else:
        return render(request, 'fileResult.html', {'filemodel': filemodel, 'usermodel': userpage_obj, 'matchfilemodel':matchfilemodel})