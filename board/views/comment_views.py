from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.forms import CommentForm
from board.models import Question, Comment


# 질문 댓글 등록
@login_required(login_url='common:login_view')
def comment_create_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()  # 댓글 작성일
            comment.author = request.user  # 댓글 작성자
            comment.question = question  # 댓글이 달린 질문
            comment.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'board/comment_form.html', context)


# 질문 댓글 삭제
@login_required(login_url='common:login_view')
def comment_delete_question(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('board:detail', question_id=comment.question.id)


# 질문 댓글 수정
@login_required(login_url='common:login_view')
def comment_modify_question(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  # 수정한 댓글
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.author = request.user
            comment.save()
            return redirect('board:detail', question_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)  # 기존 댓글
    context = {'form': form}
    return render(request, 'board/comment_form.html', context)
