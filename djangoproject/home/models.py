from django.db import models

class FileSave(models.Model):
    filename = models.CharField(max_length=30, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)

    # 제목 표시
    def __str__(self):
        return self.filename