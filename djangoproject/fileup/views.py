from django.shortcuts import redirect, render
from .models import FileUpload
from .forms import FileUploadForm

def fileUpload(request):
    if request.method == 'POST':
        return redirect('file')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        
        return render(request, 'fileupload.html', context)