# 기본관리(index, detail)
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.db.models import Q

def index(request):
    # 페이지
    page = request.GET.get('page', '1')
    # 검색어
    kw = request.GET.get('kw', '')
    # order_by(): 괄호 안의 기준으로 정렬하여 반환하는 함수
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(answer__content__icontains=kw) | # 답변 내용 검색
            Q(author__username__icontains=kw) | # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    # 페이지 당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page':page, 'kw':kw}
    # render: 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
    # 탬플릿: pybo_question_list.html
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)