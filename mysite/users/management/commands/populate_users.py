from django.contrib.auth.hashers import make_password
from users.models import CustomUser  # แก้ไข `myapp` เป็นชื่อแอปของคุณ

from django.contrib.auth.hashers import make_password

# สร้างผู้ใช้จำลอง 40 คน
users = []
for i in range(1, 41):
    users.append(CustomUser(
        first_name=f'Student{i}',
        last_name=f'LastName{i}',
        email=f'student{i}@example.com',
        username=f'student{i}',  # กำหนด username ไม่ซ้ำ
        student_id=f'12345{i:02}',  # สร้างรหัสนักศึกษาไม่ซ้ำ เช่น 1234501, 1234502
        role='student',  # กำหนด role เป็น student
        password=make_password('king090745')  # เข้ารหัสรหัสผ่าน
    ))

# บันทึกผู้ใช้ทั้งหมดในฐานข้อมูล
CustomUser.objects.bulk_create(users)
print("สร้างผู้ใช้สำเร็จแล้ว")
