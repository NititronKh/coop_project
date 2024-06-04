from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import logout


class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'student':
            return reverse('student_home')  
        elif user.role == 'teacher':
            return reverse('teacher_home')  
        elif user.role == 'staff':
            return reverse('staff_home')  
        elif user.role == 'superuser':
            return reverse('index') 
        else:
            return reverse('default_home') 
@login_required    
def logout_view(request):
    logout(request)  
    return redirect('student_home') 


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.role ='student'
            user.save()
            login(request, user)  
            return redirect('student_home')  
    else:
        form = StudentRegistrationForm()

    return render(request, 'app_users/register.html', {'form': form})
