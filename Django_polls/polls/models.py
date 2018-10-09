from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):  # 统计问题结果
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 通过外键关联question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
