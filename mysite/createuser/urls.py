from django.urls import path
from .views import *

urlpatterns =[
    path('index',index,name='index'),
    path('createsuperuser',superuser,name='createsuperuser'),
    path('createstaff',staff,name='createstaff'),
    path('createteacher',teacher,name='createteacher'),
    path('students_name',students_name,name='students_name'),
    path('staff_name',staff_name,name='staff_name'),
    path('teacher_name', teacher_name,name='teacher_name'),
    path('admin_name',admin_name,name='admin_name'),
    path("publish_delete/<int:id>",publish_delete,name= 'publish_delete'),
]