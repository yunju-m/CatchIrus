from django.urls import path
from .views import fileupload, home

urlpatterns = [
    path('', home, name='home'),
    path('file/', fileupload, name='file'),
    path('login/', login, name='login'),
    path('signUp', signUp, name='signUp'),
]
