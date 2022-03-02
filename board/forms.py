from django import forms

from board.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:  # 내부 클래스
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용'
        }
