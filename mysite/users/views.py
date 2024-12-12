from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import *


class CustomLoginView(SuccessMessageMixin, auth_views.LoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def form_invalid(self, form):
        messages.error(self.request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
        return super().form_invalid(form)

    def get_success_url(self):
        user = self.request.user
        if user.role == 'student':
            messages.success(self.request, "เข้าสู่ระบบแล้ว")
            return reverse('student_home')  
        elif user.role == 'teacher':
            messages.success(self.request, "เข้าสู่ระบบแล้ว")
            return reverse('teacher_home')  
        elif user.role == 'staff':
            messages.success(self.request, "เข้าสู่ระบบแล้ว")
            return reverse('staff_home')  
        elif user.role == 'superuser':
            messages.success(self.request, "เข้าสู่ระบบแล้ว")
            return reverse('index') 
        else:
            messages.error(self.request, "รหัสผ่านไม่ถูกต้อง")
            return reverse('default_home')
@login_required    
def logout_view(request):
    logout(request)  
    messages.success(request,"ออกจากระบบสำเร็จ")
    return redirect('student_home') 


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        
        # ตรวจสอบว่า form ถูกต้องหรือไม่
        if form.is_valid():
            # รับค่าจากฟอร์ม
            user = form.save(commit=False)
            user.role = 'student'  # กำหนดบทบาทผู้ใช้เป็น student

            # ตรวจสอบว่า student_id มีความยาวระหว่าง 12-15 ตัว
            student_id = user.student_id
            if len(student_id) < 11 or len(student_id) > 15:
                messages.error(request, "รหัสนักศึกษาต้องมีความยาวระหว่าง 12-15 ตัว")
                return render(request, 'app_users/register.html', {'form': form})

            # ตรวจสอบว่า student_id เป็นตัวเลขหรือไม่
            if not student_id.isdigit():
                messages.error(request, "รหัสนักศึกษาต้องเป็นตัวเลขเท่านั้น")
                return render(request, 'app_users/register.html', {'form': form})

            # ตรวจสอบว่า student_id ซ้ำกับที่มีอยู่ในฐานข้อมูลหรือไม่
            if CustomUser.objects.filter(student_id=student_id).exists():
                messages.error(request, "รหัสนักศึกษานี้ถูกใช้ไปแล้ว")
                return render(request, 'app_users/register.html', {'form': form})

            # บันทึกข้อมูลผู้ใช้
            user.save()

            # ทำการล็อกอินผู้ใช้
            login(request, user)

            # แสดงข้อความสำเร็จ
            messages.success(request, "ลงทะเบียนสำเร็จ! ยินดีต้อนรับเข้าสู่ระบบ")

            # เปลี่ยนเส้นทางไปที่หน้า student_home
            return redirect('student_home')
        else:
            messages.error(request, "ข้อมูลไม่ถูกต้อง กรุณาตรวจสอบข้อมูลอีกครั้ง.")
    else:
        form = StudentRegistrationForm()

    return render(request, 'app_users/register.html', {'form': form})

