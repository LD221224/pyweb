from django.db import models


# 질문 클래스(테이블) 생성
class Question(models.Model):
    question_text = models.CharField(max_length=200)    # 질문 내용
    pub_date = models.DateTimeField()                   # 작성일

    def __str__(self):
        return self.question_text


# 선택 클래스 생성
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
