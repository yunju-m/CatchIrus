from django.shortcuts import redirect, render
from .forms import FileUploadForm
from .models import FileUpload

# Create your views here.
def home(request):
    return render(request, 'home.html')

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.POST['imgfile']
        fileUpload = FileUpload(
            title = title,
            content = content,
            imgfile = img,
        )
        fileUpload.save()
        return redirect('fileupload')
    else:   # GET인 경우
        fileuploadForm = FileUploadForm()
        context = {
            'fileuploadForm' : fileuploadForm,
        }
        return render(request, 'fileupload.html', context);