from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from teacher.models import Publish
from django.contrib import messages
from django.db import IntegrityError

def home (req):
    publishes = Publish.objects.all()
    return render(req, 'staff/staff_home.html', {'publishes': publishes})

@login_required
def submit_evaluation(request):
    if request.user.role != CustomUser.STAFF:
        messages.error(request, 'คุณไม่มีสิทธิ์เข้าถึงหน้านี้')
        request.session.flush()  # เคลียร์เซสชัน
        return redirect('login')
    if request.method == 'POST':
        form = EvaluationForm(request.POST, request.FILES, evaluator=request.user)
        if form.is_valid():
            student = form.cleaned_data['student']
            if Evaluation.objects.filter(student=student, evaluator=request.user).exists():
                messages.error(request, "คุณได้ทำการประเมินนักเรียนคนนี้แล้ว")
                return redirect('already')
            try:
                evaluation = form.save(commit=False)
                evaluation.evaluator = request.user
                evaluation.save()
                messages.success(request, "ส่งการประเมินเรียบร้อยแล้ว")
                return redirect('success')
            except IntegrityError:
                messages.error(request, "เกิดข้อผิดพลาดขณะส่งการประเมิน กรุณาลองใหม่อีกครั้ง")
                return redirect('already')
    else:
        form = EvaluationForm(evaluator=request.user)
    return render(request, 'staff/evaluate_student.html', {'form': form})
@login_required
def success(req):
    return render(req,'staff/success.html')

@login_required
def already(req):
    return render(req,'staff/already.html')