from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",include("django.contrib.auth.urls")),
    path("register",view=views.student, name="register"),
    #path('login', views.login_view, name='login'),
]