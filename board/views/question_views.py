from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.forms import QuestionForm
from board.models import Question


# 질문 등록 페이지
@login_required(login_url='common:login_view')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # 내용 작성된 폼
        if form.is_valid():
            question = form.save(commit=False)  # 가저장 : create_date 없음
            question.create_date = timezone.now()  # 작성일
            question.author = request.user  # 글쓴이 : 인증된 사용자
            question.save()  # 실제 저장
            return redirect('board:boardlist')  # 저장 후 질문 목록 페이지로 이동
    else:  # request.method == 'GET':
        form = QuestionForm()  # 질문 등록 폼 객체 생성(내용 비어 있는 폼)
    context = {'form': form}
    return render(request, 'board/question_form.html', context)


# 질문 수정
@login_required(login_url='common:login_view')
def question_modify(request, question_id):
    # question = Question.objects.get(id=question_id)  # Question 가져오기
    question = get_object_or_404(Question, pk=question_id)
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


# 질문 삭제
@login_required(login_url='common:login_view')
def question_delete(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('board:boardlist')  # 질문 목록
