from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Register

class RegisterForm(UserCreationForm):
    student_id = forms.IntegerField()
    username = forms.EmailField(max_length=100 , label='email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        student_id = self.cleaned_data.get("student_id")
        Register.objects.create(user=user, student_id=student_id)
        return user

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'student_id','password1', 'password2']
