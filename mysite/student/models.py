from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone

user_model = get_user_model()

class Record(models.Model):
    # ไม่ควรตั้งค่า default ที่อ้างอิงจากโมเดลที่ยังไม่มีอยู่
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, verbose_name='ผู้ใช้')
    title = models.CharField(max_length=255, verbose_name='หัวข้อ')
    date = models.DateField(verbose_name='วันที่', default=timezone.now)
    score = models.IntegerField(verbose_name='จำนวนชั่วโมง')
    certificate = models.FileField(upload_to='certificates/', verbose_name='เอกสารรับรอง')
    STATUS_CHOICES = (
        ('pending', 'รอการอนุมัติ'),
        ('approved', 'อนุมัติ'),
        ('rejected', 'ไม่อนุมัติ'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='สถานะ')

    def __str__(self):
        return self.title

    



class Createform(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, verbose_name='ผู้ใช้')
    date2 = models.DateField(verbose_name='วันที่', default=timezone.now)
    certificate2 = models.FileField(upload_to='certificates2/', verbose_name='อัพโหลดเอกสาร', default=None)

    STATUS_CHOICES = (
        ('pending', 'รอการอนุมัติ'),
        ('approved', 'อนุมัติ'),
        ('rejected', 'ไม่อนุมัติ'),
    )
    status2 = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='สถานะ')

    
    
class AfterCompleted(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, verbose_name='ผู้ใช้')
    date3 = models.DateField(verbose_name='วันที่', default=timezone.now)
    certificate3 = models.FileField(upload_to='certificates2/', verbose_name='อัพโหลดเอกสาร', default=None)

    STATUS_CHOICES = (
        ('pending', 'รอการอนุมัติ'),
        ('approved', 'อนุมัติ'),
        ('rejected', 'ไม่อนุมัติ'),
    )
    status3 = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='สถานะ')



