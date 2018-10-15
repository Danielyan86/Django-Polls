# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


#
# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]  # 取出对象按时间排序，然后取前五个
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# use template
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question {0}."
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question %s.".format(question_id))
