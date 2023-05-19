from django.db import models

# Create your models here.
class FileSave(models.Model):
    title = models.CharField(max_length=255, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    #content = models.TextField()

    # 제목 표시
    def __str__(self):
        return self.title