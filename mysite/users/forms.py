# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'student_id', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ซ่อนข้อความตรวจสอบความถูกต้องของรหัสผ่านตั้งแต่แรก
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'data-error': False})

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        student_id = cleaned_data.get('student_id')
        
        if role == 'student' and not student_id:
            self.add_error('student_id', 'รหัสนักศึกษาเป็นฟิลด์ที่จำเป็นสำหรับนักเรียน')
        
        # ตรวจสอบว่า password1 และ password2 ถูกกรอกหรือไม่
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2:
            if password1 != password2:
                self.add_error('password2', 'รหัสผ่านไม่ตรงกัน')
        else:
            # ไม่แสดงข้อความตรวจสอบความถูกต้องของรหัสผ่านหากยังไม่ได้กรอก
            for fieldname in ['password1', 'password2']:
                if fieldname in self.errors:
                    del self.errors[fieldname]
        
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