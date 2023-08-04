from django.forms import ModelForm
from .models import FileSave, PredictProbability, RankFile, UserFile

# 업로드 파일 form, 모델 생성
class FileSaveForm(ModelForm):
    class Meta:
        model = FileSave
        fields = ('filename', 'file_upload', 'filesize')

# 사용자 별 업로드 파일 form, 모델 생성
class UserFileForm(ModelForm):
    class Meta:
        model = UserFile
        fields = ('author','authorname', 'filename', 'date')

# 파일 별 조회 횟수 form, 모델 생성
class RankFileForm(ModelForm):
    class Meta:
        model = RankFile
        fields = ('filename', 'count')

# 모델 결과 값 저장 form
class PredictProbabilityForm(ModelForm):
    class Meta:
        model = PredictProbability
        fields = ('proba',)