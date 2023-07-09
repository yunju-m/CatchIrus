from django.db import models
from django.contrib.auth.models import User

# 업로드 파일의 정보를 저장하는 모델
class FileSave(models.Model):
    filename = models.CharField(max_length=255, null=False)
    file_upload = models.FileField(upload_to="home/files/%Y/%m/%d/", blank=True)
    filesize = models.IntegerField(default=0)

    # home_filesave 이름으로 maraidb 테이블 생성 후 저장
    # 기존 db 오류 발생 시 : 초기화 작업 필요
    # python manage.py migrate --fake home(app이름) zero
    # python manage.py migrate home(app이름)
    class Meta:
        db_table = 'home_filesave'

    # 제목 표시
    def __str__(self):
        return self.filename

# 사용자 별 파일 업로드 저장 모델
class UserFile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    authorname = models.CharField(max_length=20, null=False)
    filename = models.CharField(max_length=255, null=False)
    date = models.DateTimeField()
    class Meta:
        db_table = 'user_file'