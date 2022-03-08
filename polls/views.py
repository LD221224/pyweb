from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from polls.models import Question


def index(request):
    # 자료 전체 가져오기
    question_list = Question.objects.all()
    return render(
        request,
        'polls/index.html',
        {'question_list': question_list}
    )
    # return HttpResponse("<h1>안녕~ Django!!</h1>")


@login_required(login_url='common:login')
def detail(request, pk):
    # 자료 1개 가져오기
    question = Question.objects.get(id=pk)
    return render(
        request,
        'polls/detail.html',
        {'question': question}
    )


def vote(request, pk):
    # 투표하기
    question = Question.objects.get(id=pk)
    if request.method == 'POST':
        try:
            # 선택 항목 받아오기
            choice = request.POST['choice']
        except:
            error = "항목을 선택하세요."
            return render(request, 'polls/detail.html',
                          {'question': question, 'error': error})
        else:
            # id로 db에서 검색
            sel_choice = question.choice_set.get(id=choice)
            # 1 증가
            sel_choice.votes += 1
            # 저장하기
            sel_choice.save()
            return render(request, 'polls/result.html', {'question': question})
    else:
        return render(request, 'polls/detail.html', id=pk)
