from django import forms
from django.contrib.auth import login, authenticate, get_user_model

user = get_user_model()

class Login_Form(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

class Register_Form(forms.Form):
	username = forms.CharField()
	email = forms.EmailField(widget = forms.EmailInput(
		attrs = {
		"class":"form-control", 
		"placeholder":"email"
		}
		)
	)
	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'confirm password', widget = forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = user.objects.filter(username = username)
		if qs.exists():
			raise forms.ValidationError("username is already taken")
		return username

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password!=password2:
			raise forms.ValidationError("password must match")
		return data 
