from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField()

    def __str__(self):
        return "@{}".format(self.user.username)  # แก้เป็น username หรือฟิลด์อื่นๆ ที่ต้องการแสดง
