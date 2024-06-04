from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns =[
    path('teacher_home/',views.teacher_homehome,name='teacher_home'),
    path('list_name/',views.list_name,name='list_name'),
    path("delete/<int:id>",views.delete_name ,name='delete_name'),
    path('reqrest_record/',views.reqrest_record,name='reqrest_record'),
    path('reqrest_form',views.reqrest_form,name='reqrest_form'),
    path('after',views.after,name='after'),
    path('publish/',views.publish,name='publish'),
    path("delete_publish/<int:id>",views.delete_publish,name= 'delete_publish'),
    path('delete_record/<int:id>/', views.delete_record, name='delete_record'),
    path('delete_after/<int:id>/', views.delete_after, name='delete_after'),
    path('delete_form/<int:id>/', views.delete_form, name='delete_form'),
    path('record/<int:record_id>/edit/', views.change_status, name='change_status'),
    path('form/<int:id>/edit/', views.change_status2, name='change_status2'),
    path('create_staff',views.create_staff,name='create_staff'),
    path('form/<int:id>/edit/change_status3/', views.change_status3, name='change_status3'),
    path('evaluations/', views.view_evaluations, name='evaluations'),
    path('delete_evaluations/<int:id>/', views.delete_evaluations, name='delete_evaluations'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)
