from django.contrib import admin

from .models import FileSave, UserFile

# Register your models here.
admin.site.register(FileSave)
admin.site.register(UserFile)