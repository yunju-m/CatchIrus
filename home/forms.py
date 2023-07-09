from django.forms import ModelForm
from .models import FileSave, UserFile

# 업로드 파일 form, 모델 생성
class FileSaveForm(ModelForm):
    class Meta:
        model = FileSave
        fields = ('filename', 'imgfile', 'filesize')

# 사용자 별 업로드 파일 form, 모델 생성
class UserFileForm(ModelForm):
    class Meta:
        model = UserFile
        fields = ('author','authorname', 'filename', 'date')
