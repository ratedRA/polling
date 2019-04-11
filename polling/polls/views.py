from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Choice, Question
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def main_index(request):
    return render_to_response('polls/main-index.html', {})

def index(request):
    latest_poll_list = Question.objects.all().order_by('-pub_date')[:5]

    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    p = get_object_or_404(Question, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})
    

def vote(request, poll_id):
    question = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'polls/results.html', {'question' : question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})