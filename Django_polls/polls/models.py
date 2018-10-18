from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 重写__str__方法，方便print打印输出值
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):  # 统计问题结果
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 通过外键关联question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
