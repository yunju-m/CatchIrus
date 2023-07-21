from django.urls import path
from .views import fileupload, home, detect

urlpatterns = [
    path('', home, name='home'),
    path('file/', fileupload, name='file'),
    path('detect/', detect, name='detect')
]
