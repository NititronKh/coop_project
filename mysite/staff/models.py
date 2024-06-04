from django.db import models
from django.conf import settings

class Evaluation(models.Model):
    document = models.FileField(upload_to='evaluations/')
    date = models.DateField(auto_now_add=True)
    evaluator = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='evaluation_made')
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='evaluation_received')

    def __str__(self):
        return f"Evaluation by {self.evaluator.email} for {self.student.email} on {self.date}"

