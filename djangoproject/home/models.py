from django.db import models

# 업로드 파일의 정보를 저장하는 모델
class FileSave(models.Model):
    user_id = models.ForeignKey('common.User', on_delete=models.CASCADE)
    filename = models.CharField(max_length=30, null=False)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    filesize = models.IntegerField(default=0)
    
    class Meta:
        db_table= 'home_filesave'

    # 제목 표시
    def __str__(self):
        return self.filename