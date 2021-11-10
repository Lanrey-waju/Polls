from django.shortcuts import render
from django.http import Http404
from .models import Question

# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def question_detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404('Question does not exist')
  return render(request, 'polls/detail.html', {'question': question})
