from django import forms
from .models import *

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'date', 'certificate', 'score']


from django import forms
from .models import Createform

class CreateformForm(forms.ModelForm):
    class Meta:
        model = Createform
        fields = ['date2', 'certificate2']
    
class AfterCompleteform(forms.ModelForm):
    class Meta:
        model = AfterCompleted
        fields = ['date3', 'certificate3']