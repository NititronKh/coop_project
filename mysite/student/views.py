from django.shortcuts import render,redirect,get_object_or_404
from teacher.models import *
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from django.contrib import messages
from users.models import *

def student_home(request):
    publishes = Publish.objects.all()
    return render(request, 'student/student_home.html', {'publishes': publishes})

@login_required
def record(request):
    if request.user.role != CustomUser.STUDENT:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  
        return redirect('login')
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user  
            record.save()
            messages.success(request,"บันทึกเอกสารเรียบร้อย")
            return redirect('check')  
    else:
        form = RecordForm()
    return render(request, 'student/record.html', {'form': form})

def delStudentRecord(req, id):
    # ดึงข้อมูล Record โดยใช้ ID
    post = get_object_or_404(Record, pk=id)

    # ตรวจสอบว่าผู้ใช้เป็นเจ้าของข้อมูล
    if post.user == req.user:
        if post.status == 'approved':  # ตรวจสอบสถานะของ post
            messages.error(req, "ไม่สามารถลบคำขอได้ เนื่องจากเอกสารได้รับการพิจารณาอนุมัติแล้ว")
        else:
            post.delete()  # ลบข้อมูลหากสถานะไม่ใช่ approved
            messages.success(req, "ลบคำขอบันชั่วโมงการอบรมสำเร็จ")
    else:
        messages.error(req, "คุณไม่มีสิทธิ์ลบข้อมูลนี้")
    return redirect('check')

@login_required
def check(request):
    if request.user.role != CustomUser.STUDENT:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  
        return redirect('login')
    all_records = Record.objects.filter(user=request.user)
    formstatus = Createform.objects.filter(user=request.user)
    afterform = AfterCompleted.objects.filter(user=request.user)
    approved_records = all_records.filter(status='approved')
    total_credit_hours = approved_records.aggregate(Sum('score'))['score__sum'] or 0
    return render(request, 'student/check.html', {'records': all_records, 'total_credit_hours': total_credit_hours, 'form':formstatus, 'form2':afterform})

@login_required  
def createform(req):
    if req.user.role != CustomUser.STUDENT:
        messages.error(req, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        req.session.flush()  
        return redirect('login')
    
    user_form = Createform.objects.filter(user=req.user).first()
    
    if req.method == "POST":
        if user_form: 
            form = CreateformForm(req.POST, req.FILES, instance=user_form) 
        else:
            form = CreateformForm(req.POST, req.FILES)  
        
        if form.is_valid():  
            new_form = form.save(commit=False)
            new_form.user = req.user  

            # อัปเดตสถานะเป็น 'pending' หรือค่า default
            if new_form.status2 == "approved":
                new_form.status2 = "pending"  # หรือค่าที่คุณต้องการเป็น default

            new_form.save() 
            messages.success(req, "บันทึกเอกสารเรียบร้อย")
            return redirect('check')
    else:
        if user_form:  
            form = CreateformForm(instance=user_form)
            # อัปเดตสถานะเป็น 'pending' หรือค่า default
            user_form.status2 = "pending"  # หรือค่าที่คุณต้องการเป็น default
            user_form.save()
        else:  
            form = CreateformForm()

    return render(req, 'student/createform.html', {"form": form})


@login_required  
def after_completed(req):
    if req.user.role != CustomUser.STUDENT:
        messages.error(req, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        req.session.flush()  
        return redirect('login')
    
    user_form = AfterCompleted.objects.filter(user=req.user).first()
    
    if req.method == "POST":
        if user_form: 
            form = AfterCompleteform(req.POST, req.FILES, instance=user_form) 
        else:
            form = AfterCompleteform(req.POST, req.FILES)  
        
        if form.is_valid():  
            new_form = form.save(commit=False)
            new_form.user = req.user  

            # อัปเดตสถานะเป็น 'pending' หรือค่า default
            if new_form.status3 == "approved":
                new_form.status3 = "pending"  # หรือค่าที่คุณต้องการเป็น default

            new_form.save() 
            messages.success(req, "บันทึกเอกสารเรียบร้อย")
            return redirect('check')
    else:
        if user_form:  
            afterform = AfterCompleteform(instance=user_form)
            # อัปเดตสถานะเป็น 'pending' หรือค่า default
            user_form.status3 = "pending"  # หรือค่าที่คุณต้องการเป็น default
            user_form.save()
        else:  
            afterform = AfterCompleteform()

    return render(req, 'student/after_completed.html', {"afterform": afterform})


@login_required
def delete_form(req):
    # ค้นหาฟอร์มของผู้ใช้
    user_form = get_object_or_404(Createform, user=req.user)
    if req.method == "POST":  # ลบเมื่อได้รับ POST
        user_form.delete()
        messages.error(req,"ลบเอกสารแล้ว")
        return redirect('student_home')
    return render(req, 'student/delete.html', {"form": user_form})

@login_required
def delete(request, id):
    x = get_object_or_404(Record, pk=id)
    x.delete()
    return redirect('student_home')

