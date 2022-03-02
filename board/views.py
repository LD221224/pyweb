from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from board.forms import QuestionForm
from board.models import Question


# 질문 목록 페이지
def index(request):
    # question_list = Question.objects.all()  # db에서 전체검색
    question_list = Question.objects.order_by('-create_date')  # '-' : 내림차순, '-pk'도 가능
    return render(request, 'board/question_list.html',
                  {'question_list': question_list})
    # return HttpResponse("<h2>Hello~ Django!!</h2>")


# 상세 페이지
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'board/detail.html',
                  {'question': question})


# 질문 등록 페이지
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # 내용 작성된 폼
        if form.is_valid():
            question = form.save(commit=False)  # 가저장 : create_date 없음
            question.create_date = timezone.now()
            question.save()  # 실제 저장
            return redirect('board:index')  # 저장 후 질문 목록 페이지로 이동
    else:  # request.method == 'GET':
        form = QuestionForm()  # 질문 등록 폼 객체 생성(내용 비어 있는 폼)
    return render(request, 'board/question_form.html', {'form': form})
