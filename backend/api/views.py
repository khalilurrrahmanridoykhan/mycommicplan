from django.shortcuts import render

from rest_framework import viewsets
from .models import Form, Submission
from .serializers import FormSerializer, SubmissionSerializer
from rest_framework.permissions import IsAuthenticated

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsAuthenticated]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

