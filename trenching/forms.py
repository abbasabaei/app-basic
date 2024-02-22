# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class EmailForm(forms.Form):
    submit = forms.CharField(widget=forms.PasswordInput)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField()
    supervisor_name = forms.CharField(max_length=100, required=False, label="Supervisor's Name")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','supervisor_name']

class SignInForm(AuthenticationForm):
    1
