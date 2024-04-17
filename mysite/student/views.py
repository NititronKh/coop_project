from django.shortcuts import render,redirect,get_object_or_404
from teacher.models import *
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login




# Create your views here.

def student_home(request):
    publishes = Publish.objects.all()
    return render(request, 'student/student_home.html', {'publishes': publishes})
#หน้าข้อมูลข่าวสาร

@login_required
def record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user  # กำหนดผู้ใช้ให้กับ Record เป็นผู้ใช้ปัจจุบันที่เข้าสู่ระบบ
            record.save()
            return redirect('student_home')  
    else:
        form = RecordForm()
    return render(request, 'student/record.html', {'form': form})

@login_required
def check(request):
    # ดึงข้อมูล Record ที่มีผู้ใช้ปัจจุบันที่เข้าสู่ระบบเท่านั้นและมีสถานะเป็น 'approved'
    records = Record.objects.filter(user=request.user, status='approved')
    return render(request, "student/check.html", {"records": records})

def createform(req):
    if req.method == "POST":
        form = CreateformForm(req.POST, req.FILES)  # สร้างอ็อบเจกต์ฟอร์มจากคำขอ POST
        if form.is_valid():  # ตรวจสอบความถูกต้องของข้อมูลที่ส่งมากับคำขอ POST
            form.save()  # บันทึกข้อมูลเมื่อข้อมูลถูกต้อง
            return redirect('student_home')
    else:
        form = CreateformForm()
    return render(req, 'student/createform.html', {"form": form})

def after_completed(req):
    return render(req,'student/after_completed.html')

