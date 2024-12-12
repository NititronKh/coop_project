# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# ฟอร์มสำหรับนักเรียน (Student)
class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email', 'student_id', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        student_id = cleaned_data.get('student_id')
        
        if role == 'student' and not student_id:
            self.add_error('student_id', 'รหัสนักศึกษาเป็นฟิลด์ที่จำเป็นสำหรับนักเรียน')
        
        return cleaned_data
    

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
