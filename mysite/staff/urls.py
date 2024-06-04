from django.urls import path
from . views import *

urlpatterns = [
    path('evaluate_student/', submit_evaluation, name='evaluate_student'),
    path('already',already,name='already'),
    path('staff_home',home,name='staff_home'),
    path('success',success,name='success'),
]
