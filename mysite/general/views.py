from django.shortcuts import render, redirect
from . models import *
from . forms import *

# Create your views here.
def home(req):
    return render (req,'general/home.html')
#หน้าเข้าสู่ระบบ

