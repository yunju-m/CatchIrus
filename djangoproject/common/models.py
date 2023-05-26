from django.db import models

# 회원가입 사용자 정보 저장하는 모델
# 자동으로 생성하는 user를 사용하고 있음
class User(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password1 = models.CharField(max_length=30, null=False)
    password2 = models.CharField(max_length=30, null=False)