
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
]
