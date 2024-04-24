from django.shortcuts import render,redirect,get_object_or_404
from teacher.models import *
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from django.http import HttpResponseForbidden





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
    all_records = Record.objects.filter(user=request.user)
    formstatus = Createform.objects.filter(user=request.user)
    afterform = AfterCompleted.objects.filter(user=request.user)
    approved_records = all_records.filter(status='approved')
    total_credit_hours = approved_records.aggregate(Sum('score'))['score__sum'] or 0

    return render(request, 'student/check.html', {'records': all_records, 'total_credit_hours': total_credit_hours, 'form':formstatus, 'form2':afterform})



@login_required  
def createform(req):
    user_form = Createform.objects.filter(user=req.user).first()

    if req.method == "POST":
        if user_form: 
            form = CreateformForm(req.POST, req.FILES, instance=user_form) 
        else:
            form = CreateformForm(req.POST, req.FILES)  

        if form.is_valid():  
            new_form = form.save(commit=False)
            new_form.user = req.user  
            new_form.save() 
            return redirect('check')
    else:
        if user_form:  
            form = CreateformForm(instance=user_form)
        else:  
            form = CreateformForm()

    return render(req, 'student/createform.html', {"form": form})

@login_required  
def after_completed(req):
    user_form = AfterCompleted.objects.filter(user=req.user).first()

    if req.method == "POST":
        if user_form: 
            form = AfterCompleteform(req.POST, req.FILES, instance=user_form) 
        else:
            form = AfterCompleteform(req.POST, req.FILES)  

        if form.is_valid():  
            new_form = form.save(commit=False)
            new_form.user = req.user  
            new_form.save() 
            return redirect('check')
    else:
        if user_form:  
            form = AfterCompleteform(instance=user_form)
        else:  
            form = AfterCompleteform()

    return render(req, 'student/after_completed.html', {"form": form})

@login_required
def delete_form(req):
    # ค้นหาฟอร์มของผู้ใช้
    user_form = get_object_or_404(Createform, user=req.user)
    if req.method == "POST":  # ลบเมื่อได้รับ POST
        user_form.delete()
        return redirect('student_home')

    return render(req, 'student/delete.html', {"form": user_form})


def delete(request, id):
    x = get_object_or_404(Record, pk=id)
    x.delete()
    return redirect('student_home')

