from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .forms import *
from student.models import Student


'''def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create user account
            form.save()
            # Get the username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate user and log in
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_home')  # Redirect to home page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})'''

def student(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create user account
            form.save()
            # Get the username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate user and log in
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_home')  # Redirect to home page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})

'''def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get the username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate user and log in
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student/student_home')  # Redirect to home page after successful login
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})'''
def test(req):
    return render(req,'registration/test.html')