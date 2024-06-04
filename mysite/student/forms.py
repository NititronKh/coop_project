from django import forms
from .models import *

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'date', 'certificate', 'score']
        help_texts = {
            'title': 'กรอกชื่อหัวข้ออบรม',
            'certificate': 'อัปโหลดอกสารรับรองไฟล์ pdf เท่านั้น',
            'score': 'ชั่วโมงการอบรม',
        }
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'วัน/เดือน/ปี',  # ข้อความตัวอย่าง
                    'data-date-format': '00-00-0000'  # รูปแบบวันที่
                }
            ),
        }


class CreateformForm(forms.ModelForm):
    class Meta:
        model = Createform
        fields = ['date2', 'certificate2']
        widgets = {
            'date2': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'วัน/เดือน/ปี',  # ข้อความตัวอย่าง
                    'data-date-format': '00-00-0000'  # รูปแบบวันที่
                }
            ),
        }
    
class AfterCompleteform(forms.ModelForm):
    class Meta:
        model = AfterCompleted
        fields = ['date3', 'certificate3']
        widgets = {
            'date3': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'วัน/เดือน/ปี',  # ข้อความตัวอย่าง
                    'data-date-format': '00-00-0000'  # รูปแบบวันที่
                }
            ),
        }