from django.shortcuts import render ,redirect,get_object_or_404
from general.models import *
from student.models import *
from .models import *
from .forms import *
from django.contrib.auth.models import User
from student.forms import *
from users.forms import RegisterForm
# Create your views here.

def teacher_homehome(req):
    publishes = Publish.objects.all()
    return render(req, 'teacher/teacher_home.html', {'publishes': publishes})


def list_name(request):
    list = User.objects.all()
    return render(request, 'teacher/list_name.html', {'list': list})

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

def delete_record(request, id):
    coop = get_object_or_404(Record, pk=id)
    coop.delete()
    return redirect('reqrest_record')

def change_status(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'POST':

        # แค่บางฟิลด์เท่านั้นที่มีการแก้ไข
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
    return render(req,'teacher/reqrest_form.html',{"form" : form})

