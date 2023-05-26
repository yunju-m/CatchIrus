from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 사용자 계정 생성시 사용할 UserForm
# UserCreationForm을 상속받음
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("id", "username", "password1", "password2")