from django.db import models

# Create your models here.
class FileUpload(models.Model):
    #filesave = models.ForeignKey(FileSave, on_delete=models.CASCADE)
    file_title = models.CharField(max_length=255, null=True)
    file_imgfile = models.ImageField(null=True, upload_to="", blank=True)
    #content = models.TextField()

    # 제목 표시
    def __str__(self):
        return self.file_title
    
