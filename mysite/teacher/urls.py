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
    path('create_user',views.create_user,name='create_user'),
    path('publish/',views.publish,name='publish'),
    path("delete_publish/<int:id>",views.delete_publish,name= 'delete_publish'),
    path('delete/<int:id>/', views.delete_record, name='delete_record'),
    path('record/<int:record_id>/edit/', views.change_status, name='change_status'),
    path('form/<int:id>/edit/', views.change_status2, name='change_status2')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)
