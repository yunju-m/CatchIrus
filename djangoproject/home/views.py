from . import models
from django.shortcuts import redirect, render
from .models import FileSave
from .forms import FileSaveForm
from django.http import JsonResponse

def home(request):
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

    else:
        # model의 기존 값들을 모두 제거하여 새롭게 입력한 값들만 출력
        models.FileSave.objects.all().delete() 
        filesaveForm = FileSaveForm
        context = {
            'filesaveForm': filesaveForm,
        }
        return render(request, 'home.html', context)
    
def fileupload(request):
    model = models.FileSave.objects.all()
    return render(request, 'fileResult.html', {'model': model})