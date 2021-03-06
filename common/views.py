from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from common.forms import UserForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # db와 비교해 인증 처리
        user = authenticate(username=username, password=password)
        if user is not None:  # user가 있다면(일치하면)
            login(request, user)  # 로그인
            return redirect('board:index')
        else:
            error = "아이디나 비밀번호가 일치하지 않습니다."
            return render(request, 'common/login.html', {'error': error})
    else:
        return render(request, 'common/login.html')


def logout_view(request):
    logout(request)
    return redirect('board:index')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # 회원 가입 후 자동 로그인
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('board:index')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)


def send_email(request):
    return render(request, 'common/send_email.html')
