# accounts/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout
from users.forms import *
from users.models import *
from teacher.models import Publish
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def index(request):
    if request.user.role != CustomUser.SUPERUSER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  
        return redirect('login')
    publishes = Publish.objects.all()
    return render(request, 'createuser/index.html', {'publishes': publishes})
@login_required
def teacher(request):
    if request.user.role != CustomUser.SUPERUSER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        logout(request)
        return redirect('login')
    
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'teacher'
            user.save()
            messages.success(request, 'บัญชีผู้ใช้ครูถูกสร้างเรียบร้อยแล้ว')
            return redirect('teacher_name')
    else:
        form = TeacherRegistrationForm()
    
    return render(request, 'createuser/createteacher.html', {'form': form})

# View สำหรับลงทะเบียนเจ้าหน้าที่
@login_required
def staff(request):
    if request.user.role != CustomUser.SUPERUSER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        logout(request)  # ใช้ logout แทนการ flush เซสชัน
        return redirect('login')
    
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'staff'
            user.save()
            messages.success(request, 'บัญชีผู้ใช้ staff ถูกสร้างเรียบร้อยแล้ว')
            return redirect('staff_name')
    else:
        form = StaffRegistrationForm()
    
    return render(request, 'createuser/createstaff.html', {'form': form})
@login_required
def superuser(request):
    if request.user.role != CustomUser.SUPERUSER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        logout(request)  # ใช้ logout แทนการ flush เซสชัน
        return redirect('login')
    
    if request.method == 'POST':
        form = SuperuserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = CustomUser.SUPERUSER
            user.save()
            messages.success(request, 'บัญชีผู้ใช้ superuser ถูกสร้างเรียบร้อยแล้ว')
            return redirect('index')
    else:
        form = SuperuserRegistrationForm()
    
    return render(request, 'createuser/createsuperuser.html', {'form': form})

def students_name(request):
    students = CustomUser.objects.filter(role=CustomUser.STUDENT)
    return render(request, 'createuser/student_name.html', {'students': students})
def staff_name(request):
    staff = CustomUser.objects.filter(role=CustomUser.STAFF)
    return render(request, 'createuser/staff_name.html', {'staff': staff})
def teacher_name(request):
    teacher = CustomUser.objects.filter(role=CustomUser.TEACHER)
    return render(request, 'createuser/teacher_name.html', {'teacher': teacher})
def admin_name(request):
    admin = CustomUser.objects.filter(role=CustomUser.SUPERUSER)
    return render(request, 'createuser/admin_name.html', {'admin': admin})
@login_required
def publish_delete(request, id):
    coop = get_object_or_404(Publish, pk=id)
    coop.delete()
    return redirect('index')
