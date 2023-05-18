from django.urls import path
from .views import fileUpload

urlpatterns = [
	path('', fileUpload, name="fileup"),
]