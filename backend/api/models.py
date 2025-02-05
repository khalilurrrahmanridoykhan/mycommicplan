from django.db import models
from django.contrib.auth.models import User

class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Submission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    data = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)

