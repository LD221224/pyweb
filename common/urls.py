from django.urls import path
from django.contrib.auth import views as auth_view

from . import views

app_name = 'common'

urlpatterns = [
    # 로그인 LoginView 클래스 - 제네릭 뷰
    # path('login/', auth_view.LoginView.as_view(template_name='common/login.html'),
    #      name='login'),
    # 로그아웃
    # path('logout/', auth_view.LogoutView.as_view(), name='logout'),

    # 로그인 - 함수형 뷰
    path('login/', views.login_view, name='login_view'),
    # 로그아웃
    path('logout/', views.logout_view, name='logout_view'),
    # 회원 가입
    path('signup/', views.signup, name='signup'),
]
