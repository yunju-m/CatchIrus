from django.forms import ModelForm
from .models import FileSave

class FileSaveForm(ModelForm):
    class Meta:
        model = FileSave
        fields = ['filename', 'imgfile']