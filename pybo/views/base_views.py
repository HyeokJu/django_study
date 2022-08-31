# 기본관리(index, detail)
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question

def index(request):
    # 페이지
    page = request.GET.get('page', '1')
    # order_by(): 괄호 안의 기준으로 정렬하여 반환하는 함수
    question_list = Question.objects.order_by('-create_date')
    # 페이지 당 10의 데이터 보여주기
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    # render: 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
    # 탬플릿: pybo_question_list.html
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)