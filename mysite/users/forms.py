# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# ฟอร์มสำหรับนักเรียน (Student)
class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email', 'student_id', 'password1', 'password2']

# ฟอร์มสำหรับครู (Teacher)
class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email', 'password1', 'password2']

# ฟอร์มสำหรับเจ้าหน้าที่ (Staff)
class StaffRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email', 'password1', 'password2']

# ฟอร์มสำหรับผู้ดูแลระบบ (Superuser)
class SuperuserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','password1', 'password2']
