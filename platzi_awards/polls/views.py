
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice


# Create your views here.

# def index (request):
    # latest_question_list = Question.objects.all()
    # return render(request, 'polls/index.html', {
        # 'latest_question_list': latest_question_list
        # })

class IndexView (generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset (self):
        """ Return the List of Published Questions """
        return Question.objects.filter(publication_date__lte=timezone.now()).order_by("-publication_date")

class DetailView (generic.DetailView):
    model = Question
    template_name = 'polls/question_info.html'

    def get_queryset(self):
        return Question.objects.filter(publication_date__lte=timezone.now())

class ResultsView (DetailView):
    template_name = 'polls/question_count.html'


# def question_info (request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/question_info.html', {
        # 'question': question
        # })



# def question_count (request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/question_count.html', {
        # 'question': question
        # })


def question_vote (request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExists):
        return render(request, 'polls/question_info.html', {
            'question': question,
            'error_message': 'Question\'s Choice not Selected'
            })

    selected_choice.choice_votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:q_count', args=[question.id]))
