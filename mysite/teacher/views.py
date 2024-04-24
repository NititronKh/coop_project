from django.shortcuts import render ,redirect,get_object_or_404

from .models import *
from .forms import *
from django.contrib.auth.models import User
from student.forms import *
from django.db.models import Sum
# Create your views here.

def teacher_homehome(req):
    publishes = Publish.objects.all()
    return render(req, 'teacher/teacher_home.html', {'publishes': publishes})


    
def list_name(request):
    # ดึงผู้ใช้ทั้งหมดและ Prefetch Createform สำหรับแต่ละ User
    users = User.objects.all().prefetch_related('createform_set')
    
    # สร้างข้อมูลสำหรับส่งไปยัง template
    user_data = []

    for user in users:
        # ดึงเฉพาะ Record ที่ได้รับการอนุมัติ
        approved_records = Record.objects.filter(user=user, status='approved')

        # คำนวณคะแนนรวมของ 'approved' Records
        total_approved_score = approved_records.aggregate(Sum('score'))['score__sum'] or 0
        
        # ดึงฟอร์มที่เกี่ยวข้องกับผู้ใช้นี้
        form1 = Createform.objects.filter(user=user)
        form2 = AfterCompleted.objects.filter(user=user)

        # เก็บข้อมูลที่ต้องการลงใน user_data
        user_data.append({
            'user': user,
            'total_approved_score': total_approved_score,
            'form1': form1,
            'form2':form2
        })

    # ส่งข้อมูลไปยัง template
    return render(request, 'teacher/list_name.html', {'user_data': user_data})
def delete_name(request, id):
    x = get_object_or_404(User, pk=id)
    x.delete()
    return redirect('list_name')


def publish(request):
    if request.method == 'POST':
        form = PublishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('teacher_home')
    else:
        form = PublishForm()

    return render(request, 'teacher/publish.html', {'form': form})

def delete_publish(request, id):
    x = get_object_or_404(Publish, pk=id)
    x.delete()
    return redirect('teacher_home')

def reqrest_record(request):
    coops = Record.objects.all()
    total_credit_hours = Record.objects.aggregate(total_credit_hours=models.Sum('score'))['total_credit_hours']
    return render(request, 'teacher/reqrest_record.html', {'coops': coops, 'total_credit_hours': total_credit_hours})
def create_user(req):
    return render(req,'teacher/create_user.html')


def change_status(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'POST':
        record.status = 'approved' 

        record.save(update_fields=['status'])       
    ##return render(request, 'teacher/edit_record.html', {'form': form})
    return redirect('reqrest_record')

def change_status2(request, id):
    form = get_object_or_404(Createform, pk=id)
    if request.method == 'POST':

        # แค่บางฟิลด์เท่านั้นที่มีการแก้ไข
        form.status2 = 'approved'
        form.save(update_fields=['status2']) 
            
    ##return render(request, 'teacher/edit_record.html', {'form': form})
    return redirect('reqrest_form')

def reqrest_form(req):
    form = Createform.objects.all()
    name = User.objects.all()
    
    context = {
        "form": form,
        "name": name
    }
    
    return render(req, 'teacher/reqrest_form.html', context)

def reqrest_form(request):
    # ดึงข้อมูลผู้ใช้ทั้งหมด
    users = User.objects.all()
    
    # เตรียมข้อมูลสำหรับการส่งไปยังเทมเพลต
    user_forms_data = []

    # วนลูปผ่านผู้ใช้แต่ละคน
    for user in users:
        # ดึงข้อมูลฟอร์มที่เชื่อมโยงกับผู้ใช้คนนี้
        user_forms = Createform.objects.filter(user=user)

        # เพิ่มข้อมูลผู้ใช้และฟอร์มที่เกี่ยวข้องลงในลิสต์
        user_forms_data.append({
            'user': user,
            'forms': user_forms
        })

    # ส่งข้อมูลไปยังเทมเพลต
    return render(request, 'teacher/reqrest_form.html', {'user_forms_data': user_forms_data})

def delete_record(request, id):
    coop = get_object_or_404(Record, pk=id)
    coop.delete()
    return redirect('reqrest_form')
def delete_form(req,id):
    i = get_object_or_404(Createform,pk=id)
    i.delete()
    return redirect('create_form')

