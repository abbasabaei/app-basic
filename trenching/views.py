from .forms import SignUpForm,SignInForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
def home(request):
    return render(request,'trenching/home.html')
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            supervisor_name = form.cleaned_data['supervisor_name']
            print(supervisor_name)
            # Optionally, you can log in the user after sign-up
            # For example:
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
              # Redirect to home page after sign-up
    else:
        form = SignUpForm()
    return render(request, 'trenching/signup.html', {'form': form})



def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')  # Redirect to home page after successful sign-in
    else:
        form = SignInForm()
    return render(request, 'trenching/signin.html', {'form': form})