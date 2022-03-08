from django.urls import path
from . import views

# 네임 스페이스(소속)
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),              # 127.0.0.1:8000/polls/
    path('<int:pk>/', views.detail, name='detail'),   # 127.0.0.1:8000/polls/1/
    path('<int:pk>/vote/', views.vote, name='vote')   # 127.0.0.1:8000/polls/1/vote/
]
