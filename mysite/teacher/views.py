from django.shortcuts import render ,redirect,get_object_or_404
from .models import *
from .forms import *
from student.forms import *
from django.db.models import Sum
from users.models import *
from staff.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout
from users.models import *
from users.forms import *
from django.contrib import messages

@login_required
def teacher_homehome(req):
    if req.user.role != CustomUser.TEACHER:
        messages.error(req, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        req.session.flush()  # เคลียร์เซสชัน
        return redirect('login')  
    publishes = Publish.objects.all()
    return render(req, 'teacher/teacher_home.html', {'publishes': publishes})

@login_required
def list_name(request):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')

    # ดึงค่าตัวกรองสถานะจาก POST
    status_filter = request.POST.get("status_filter")

    students = CustomUser.objects.filter(role='student').prefetch_related('createform_set')
    student_data = []

    for student in students:
        # คำนวณคะแนนที่ได้รับการอนุมัติ
        approved_records = Record.objects.filter(user=student, status='approved')
        total_approved_score = approved_records.aggregate(Sum('score'))['score__sum'] or 0

        # ดึงฟอร์ม AfterCompleted (form2)
        form1 = Createform.objects.filter(user=student)
        form2 = AfterCompleted.objects.filter(user=student)

        # กรองข้อมูลตามตัวกรองสถานะ
        if status_filter == "approved":
            form2 = form2.filter(status3='approved')
        elif status_filter == "pending":
            form2 = form2.filter(status3='pending')
        elif status_filter == "no_data":
            # กรณีไม่มีข้อมูลใน form2
            form2 = form2.none()
        elif status_filter:  # ถ้ามีสถานะอื่นที่ไม่รองรับ
            form2 = form2.none()

        # ตรวจสอบว่า form2 มีข้อมูลตรงตามเงื่อนไข หรือเป็นกรณี "ไม่มีข้อมูล"
        if form2.exists() or (status_filter == "no_data" and not AfterCompleted.objects.filter(user=student).exists()) or not status_filter:
            student_data.append({
                'user': student,
                'total_approved_score': total_approved_score,
                'form1': form1,
                'form2': form2,
            })

    return render(request, 'teacher/list_name.html', {
        'user_data': student_data,
        'selected_status': status_filter
    })


@login_required
def delete_name(request, id):
    x = get_object_or_404( CustomUser, pk=id)
    x.delete()
    messages.error(request,'ลบผู้ใช้แล้ว')
    return redirect('list_name')

@login_required
def publish(request):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')
    if request.method == 'POST':
        form = PublishForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user 
            record.save()
            messages.success(request,"ประกาศข่าวสารแล้ว")
            return redirect('teacher_home')  
    else:
        form = PublishForm()
    return render(request, 'teacher/publish.html', {'form': form})

@login_required
def delete_publish(request, id):
    post = get_object_or_404(Publish, pk=id)
    if post.user == request.user:  
        post.delete()
        messages.error(request,'ประกาศถูกลบแล้ว')
    return redirect('teacher_home')


@login_required
def reqrest_record(request):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')
    coops = Record.objects.all()
    total_credit_hours = Record.objects.aggregate(total_credit_hours=models.Sum('score'))['total_credit_hours']
    return render(request, 'teacher/reqrest_record.html', {'coops': coops, 'total_credit_hours': total_credit_hours})


@login_required
def change_status(request, record_id):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')
    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'POST':
        record.status = 'approved' 

        record.save(update_fields=['status'])  
        messages.success(request,"อนุมัติคำขอแล้ว")     
    return redirect('reqrest_record')

@login_required
def change_status2(request, id):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')
    form = get_object_or_404(Createform, pk=id)

    if request.method == 'POST':
        new_status = request.POST.get('status', None)  # รับค่า 'status' จาก POST

        if new_status in ['approved', 'rejected']:  # ตรวจสอบว่าค่าเป็นหนึ่งในตัวเลือกที่อนุญาต
            form.status2 = new_status
            form.save(update_fields=['status2'])
            messages.success(request,"อนุมัติคำขอแล้ว")  

    return redirect('reqrest_form') 
@login_required
def change_status3(request, id):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')

    form = get_object_or_404(AfterCompleted, pk=id)

    if request.method == 'POST':
        new_status = request.POST.get('status', None)

        if new_status in ['approved', 'rejected']:
            form.status3 = new_status
            form.save(update_fields=['status3'])
            messages.success(request,"อนุมัติคำขอแล้ว")  

    return redirect('after') 


@login_required
def reqrest_form(request):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')
    users = CustomUser.objects.all()
    user_forms_data = []
    for user in users:
        user_forms = Createform.objects.filter(user=user)
        user_forms_data.append({
            'user': user,
            'forms': user_forms
        })
    return render(request, 'teacher/reqrest_form.html', {'user_forms_data': user_forms_data})

@login_required
def after(request):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')
    users = CustomUser.objects.all()
    user_forms_data = []
    for user in users:
        user_forms = AfterCompleted.objects.filter(user=user)
        user_forms_data.append({
            'user': user,
            'forms': user_forms
        })
    return render(request, 'teacher/after.html', {'user_forms_data': user_forms_data})
@login_required
def delete_record(request, id):
    coop = get_object_or_404(Record, pk=id)
    coop.delete()
    messages.success(request,"ลบคำขอเสร็จสิ้น")
    return redirect('reqrest_record')

@login_required
def delete_form(req,id):
    i = get_object_or_404(Createform,pk=id)
    i.delete()
    messages.error(req,"ลบคำขอเสร็จสิ้น")
    return redirect('reqrest_form')
@login_required
def delete_after(req,id):
    i = get_object_or_404(AfterCompleted,pk=id)
    i.delete()
    messages.error(req,"ลบคำขอเสร็จสิ้น")
    return redirect('after')


@login_required
def create_staff(request):
    if request.user.role != CustomUser.TEACHER:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        logout(request)  # ใช้ logout แทนการ flush เซสชัน
        return redirect('login')
    
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'staff'
            user.save()
            messages.success(request, 'บัญชีผู้ใช้พี่เลี้ยง ถูกสร้างเรียบร้อยแล้ว')
            # Teacher สร้างเสร็จแล้ว redirect ไปที่หน้า home ของ teacher
            return redirect('teacher_home')
    else:
        form = StaffRegistrationForm()
    
    return render(request, 'teacher/createuser.html', {'form': form})

@login_required
def view_evaluations(request):
    evaluations = Evaluation.objects.all()
    return render(request, 'teacher/evaluations.html', {'evaluations': evaluations})

@login_required
def delete_evaluations(request, id):
    x = get_object_or_404(Evaluation, pk=id)
    x.delete()
    messages.error(request,"ลบผลการประเมินแล้ว")
    return redirect('evaluations')