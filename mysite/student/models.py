from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Record(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, verbose_name='ผู้ใช้', default=user_model.objects.first().id)
    title = models.CharField(max_length=255, verbose_name='หัวข้อ')
    date = models.DateField(verbose_name='วันที่')
    score = models.IntegerField(verbose_name='จำนวนชั่วโมง')
    certificate = models.FileField(upload_to='certificates/', verbose_name='เอกสารรับรอง')
    STATUS_CHOICES = (
        ('pending', 'รอการอนุมัติ'),
        ('approved', 'อนุมัติ'),
        ('rejected', 'ไม่อนุมัติ'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='สถานะ')

    @property
    def status_display(self):
        if self.status == 'approved':
            return 'อนุมัติแล้ว'
        elif self.status == 'rejected':
            return 'ไม่อนุมัติ'
        else:
            return 'รอการอนุมัติ'

    def __str__(self):
        return self.title

    

from django.db import models
from django.utils import timezone

class Createform(models.Model):
    date2 = models.DateField(verbose_name='วันที่', default=timezone.now)
    certificate2 = models.FileField(upload_to='certificates2/', verbose_name='อัพโหลดเอกสาร', default=None)

    STATUS_CHOICES = (
        ('pending', 'รอการอนุมัติ'),
        ('approved', 'อนุมัติ'),
        ('rejected', 'ไม่อนุมัติ'),
    )
    status2 = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='สถานะ')

    def __str__(self):
        return self.title
    
class Student(models.Model):
    student_id = models.IntegerField(max_length=15)
