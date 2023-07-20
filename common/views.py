from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# 새로운 사용자 정보를 저장하여 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/common/login')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})