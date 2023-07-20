from django.contrib import admin

from .models import FileSave, UserFile, RankFile

# Register your models here.
admin.site.register(FileSave)
admin.site.register(UserFile)
admin.site.register(RankFile)