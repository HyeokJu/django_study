from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    # CharField: 글자수의 길이가 제한된 텍스트
    content = models.TextField()
    # TextField: 글자수의 길이 제한이 없는 텍스트
    create_date = models.DateTimeField()
    # DateTimeField: 날짜와 시간에 관계된 속성
    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey: 다른 모델을 연결하기 위해 사용
    # on_delete=models.CASCADE: 답변과 연결된 질문이 삭제될 경우 함께 삭제
    # CASCADE: 한 질문에 연결된 모든 답변 삭제
    content = models.TextField()
    create_date = models.DateTimeField()


