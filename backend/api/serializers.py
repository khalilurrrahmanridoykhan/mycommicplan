# idoy/Documents/mycommicplan/backend/api/serializers.py
from rest_framework import serializers
from .models import Project, Form, FormAccess, Setting, Submission

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class FormAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAccess
        fields = '__all__'

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    forms = FormSerializer(many=True, read_only=True)
    form_access = FormAccessSerializer(many=True, read_only=True)
    settings = SettingSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['name', 'description', 'forms', 'form_access', 'settings']  # Exclude 'id'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'