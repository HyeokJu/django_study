from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
# Create your views here.

def index(request):
    # order_by(): 괄호 안의 기준으로 정렬하여 반환하는 함수
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # render: 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
    # 탬플릿: pybo_question_list.html
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question에 대한 답변 생성, Question과 Answer 모델이 foreign key로 연결되어 있기 때문에 가능
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)