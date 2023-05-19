from django.shortcuts import redirect, render
from .models import FileSave
from .forms import FileSaveForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        #title = request.POST['title']
        #content = request.POST['content']
        imgfile = request.FILES["input-file"]
        filesave = FileSave(
            #title=title,
            #content=content,
            imgfile=imgfile,
        )
        filesave.save()
        return redirect('file')
    else:
        filesaveForm = FileSaveForm
        context = {
            'filesaveForm': filesaveForm,
        }
        return render(request, 'home.html', context)