from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student_home/', views.student_home, name='student_home'),
    path('record/', views.record, name='record'),
    path('createform/', views.createform, name='createform'),
    path('check/', views.check, name='check'),
    path('after_completed/', views.after_completed, name='after_completed'),
    # สร้าง URL pattern สำหรับไฟล์สื่อ
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)