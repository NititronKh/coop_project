from django import forms
from .models import *

class PublishForm(forms.ModelForm):
    class Meta:
        model = Publish
        fields = ['title', 'content', 'image']

