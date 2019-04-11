from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Choice, Question
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from .forms import  Login_Form, Register_Form
from django.contrib.auth import login, authenticate, get_user_model, logout


user = get_user_model()
def main_index(request):
    return render(request, 'polls/main-index.html', {})

def index(request):
    latest_poll_list = Question.objects.all().order_by('-pub_date')[:5]
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
    	print('istyes')
    	return render(request, 'polls/index.html', {'latest_poll_list': latest_poll_list})
    else:
    	print('2ndyes')
    	return render(request, 'polls/index.html', {'latest_poll_list': 'login'})


def detail(request, poll_id):
    p = get_object_or_404(Question, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': p})
    

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


def login_page(request):
	login_form = Login_Form(request.POST or None)
	context = {
	'form' : login_form
	}
	print("user logged in")
	print(request.user.is_authenticated())
	if login_form.is_valid():
		print('yes')
		print(login_form.cleaned_data)
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')
		print(request.user.is_authenticated())
		user = authenticate(request, username = username, password = password)
		print(request.user.is_authenticated())
		if user is not None:
			login(request, user)
			print(request.user.is_authenticated())
			#context['form'] = Login_Form()
			return redirect("/polls/")
		else:
			print('Error')
	
	return render(request, 'auth/login.html', context)


def register_page(request):
	register_form = Register_Form(request.POST or None)
	context = {
	'form' : register_form
	}
	if register_form.is_valid():
		print(register_form.cleaned_data)
		username = register_form.cleaned_data.get('username')
		email = register_form.cleaned_data.get('email')
		password = register_form.cleaned_data.get('password')
		new_user = user.objects.create_user(username, email, password)
		print(new_user)
	return render(request, 'auth/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')
