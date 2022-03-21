from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from board.models import Question


# 질문 추천
@login_required(login_url='common:login_view')
def vote_question(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    elif request.user in question.voter.all():
        messages.error(request, "이미 추천한 글 입니다.")
    else:
        question.voter.add(request.user)  # 추천 1 증가
    return redirect('board:detail', question_id=question_id)
