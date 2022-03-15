from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from board.models import Question


# 인덱스 페이지
def index(request):
    question_list = Question.objects.order_by('-pk')[:3]  # 최근 3개의 Question
    context = {'question_list': question_list}
    return render(request, 'board/index.html', context)


# 질문 목록 페이지
def boardlist(request):
    # question_list = Question.objects.all()  # db에서 전체검색
    question_list = Question.objects.order_by('-create_date')  # '-' : 내림차순, '-pk'도 가능

    # 페이징 처리
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)  # 페이지당 Question 10개
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}

    return render(request, 'board/question_list.html', context)
    # return HttpResponse("<h2>Hello~ Django!!</h2>")


# 상세 페이지
def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)  # url 경로 오류 처리
    context = {'question': question}
    return render(request, 'board/detail.html', context)
