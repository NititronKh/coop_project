
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    STUDENT = 'student'
    TEACHER = 'teacher'
    STAFF = 'staff'
    SUPERUSER = 'superuser'
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (STAFF, 'Staff'),
        (SUPERUSER, 'Superuser'),
    ]
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=SUPERUSER)
    student_id = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=150, unique=False, blank=True)  # ไม่ให้ซ้ำกันและสามารถเป็นค่าว่าง

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
