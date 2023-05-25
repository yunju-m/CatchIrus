from django.forms import ModelForm
from .models import FileSave

# 업로드 파일 form, 모델 생성
class FileSaveForm(ModelForm):
    class Meta:
        model = FileSave
        fields = ['filename', 'imgfile', 'filesize']