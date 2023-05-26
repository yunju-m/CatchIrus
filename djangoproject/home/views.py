from . import models
from django.shortcuts import redirect, render
from .models import FileSave
from .forms import FileSaveForm
from common.forms import UserForm

def home(request):
    # 제출버튼을 클릭하면 해당 file정보를 저장하고 /file로 매핑
    if request.method == 'POST':
        imgfile = request.FILES["input-file"]
        filename = request.FILES["input-file"].name
        filesize = request.FILES["input-file"].size
        filesave = FileSave(
            filename = filename,
            imgfile = imgfile,
            filesize = filesize,
        )
        filesave.save()
        return redirect('file')
    # 홈페이지를 불러오면 form생성하고 home.html 화면 출력
    else:
        # model의 기존 값들을 모두 제거하여 새롭게 입력한 값들만 출력
        models.FileSave.objects.all().delete() 
        userForm = UserForm
        filesaveForm = FileSaveForm
        context = {
            'userForm': userForm,
            'filesaveForm': filesaveForm,
        }
        return render(request, 'home.html', context)

# /file 매핑되면 file 정보를 fileResult.html에 출력    
def fileupload(request):
    model = models.FileSave.objects.all()
    return render(request, 'fileResult.html', {'model': model})