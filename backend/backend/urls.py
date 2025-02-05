from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import FormViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'forms', FormViewSet)
router.register(r'submissions', SubmissionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
