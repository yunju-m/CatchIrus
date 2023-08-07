from django.urls import path
from .views import filechart, fileupload, home

urlpatterns = [
    path('', home, name='home'),
    path('file/', fileupload, name='file'),
    path('file/chart', filechart, name='filechart')
]
