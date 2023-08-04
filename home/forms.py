from django.forms import ModelForm
from .models import FileSave, UserFile, PredictProbability

# 업로드 파일 form, 모델 생성
class FileSaveForm(ModelForm):
    class Meta:
        model = FileSave
        fields = ('filename', 'file_upload', 'filesize', 'result')

# 사용자 별 업로드 파일 form, 모델 생성
class UserFileForm(ModelForm):
    class Meta:
        model = UserFile
        fields = ('author','authorname', 'filename', 'date')

# 파일 예측 퍼센트 form, 모델 생성
class PredictProbabilityForm(ModelForm):
    class Meta:
        model = PredictProbability
        fields = ('proba',)