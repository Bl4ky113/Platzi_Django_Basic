
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index (request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list
        })


def question_info (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/question_info.html', {
        'question': question
        })
        


def question_count (request, question_id):
    return HttpResponse(f'This is the Question Num {question_id} Vote Count')


def question_vote (request, question_id):
    return HttpResponse(f'Voting Question Num {question_id}')
