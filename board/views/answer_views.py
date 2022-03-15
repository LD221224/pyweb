from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.forms import AnswerForm
from board.models import Question, Answer


# 답변 등록
@login_required(login_url='common:login_view')
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


# 답변 수정
@login_required(login_url='common:login_view')
def answer_modify(request, answer_id):
    # answer = Answer.objects.get(id=answer_id)
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.author = request.user
            answer.save()
            return redirect('board:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'form': form}
    return render(request, 'board/answer_form.html', context)


# 답변 삭제
@login_required(login_url='common:login_view')
def answer_delete(request, answer_id):
    # answer = Answer.objects.get(id=answer_id)
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('board:detail', question_id=answer.question.id)  # 상세 페이지
