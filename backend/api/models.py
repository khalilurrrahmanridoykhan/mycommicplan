# backend/api/models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Form(models.Model):
    project = models.ForeignKey(Project, related_name='forms', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Add other form fields here

class Submission(models.Model):
    form = models.ForeignKey(Form, related_name='submissions', on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class FormAccess(models.Model):
    project = models.ForeignKey(Project, related_name='form_access', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    access_level = models.CharField(max_length=50)
    # Add other access fields here

class Setting(models.Model):
    project = models.ForeignKey(Project, related_name='settings', on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    # Add other settings fields here