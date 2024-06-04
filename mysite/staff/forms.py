from django import forms
from .models import Evaluation
from django.contrib.auth import get_user_model
from users.models import CustomUser

User = get_user_model()

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['document', 'student']

    def __init__(self, *args, **kwargs):
        evaluator = kwargs.pop('evaluator', None)
        super().__init__(*args, **kwargs)
        if evaluator:
            self.fields['student'].queryset = CustomUser.objects.filter(role=CustomUser.STUDENT)
