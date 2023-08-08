from django.urls import path
from .views import fileupload, home, modalfileupload

urlpatterns = [
    path('', home, name='home'),
    path('file/', fileupload, name='file'),
    path('modalfile/', modalfileupload, name='modalfile'),
]
