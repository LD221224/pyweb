from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from board.forms import QuestionForm, AnswerForm
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
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)  # url 경로 오류 처리
    context = {'question': question}
    return render(request, 'board/detail.html', context)


# 질문 등록 페이지
@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # 내용 작성된 폼
        if form.is_valid():
            question = form.save(commit=False)  # 가저장 : create_date 없음
            question.create_date = timezone.now()  # 작성일
            question.author = request.user  # 글쓴이 : 인증된 사용자
            question.save()  # 실제 저장
            return redirect('board:index')  # 저장 후 질문 목록 페이지로 이동
    else:  # request.method == 'GET':
        form = QuestionForm()  # 질문 등록 폼 객체 생성(내용 비어 있는 폼)
    context = {'form': form}
    return render(request, 'board/question_form.html', context)


# 답변 등록
@login_required(login_url='common:login')
def answer_create(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question_id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board/detail.html', context)


# 질문 수정
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = Question.objects.get(id=question_id)  # Question 가져오기
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)  # 새로 작성한 폼
        if form.is_valid():
            question = form.save(commit=False)  # 가저장
            question.modify_date = timezone.now()  # 수정일
            question.author = request.user  # 글쓴이
            question.save()  # 실저장
            return redirect('board:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)  # 작성된 폼 가져오기
    context = {'form': form}
    return render(request, 'board/question_form.html', context)
