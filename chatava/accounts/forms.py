from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
	first_name = forms.CharField(max_length=64, required=False, widget=forms.TextInput())
	#name = forms.CharField(max_length=64, required=False, widget=forms.TextInput(attrs={"placeholder": "Optional"}))
	last_name = forms.CharField(max_length=64, required=False, widget=forms.TextInput())
	#username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Required*"}))
	class Meta:
			model = User
			fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
