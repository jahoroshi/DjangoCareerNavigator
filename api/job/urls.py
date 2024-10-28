from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.job.views import JobVacViewSet, JobRequiredSkillViewSet

router = DefaultRouter()
# router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'opening', JobVacViewSet, basename='jobs')
router.register(r'requirements', JobRequiredSkillViewSet, basename='requirements')

urlpatterns = [
    path('', include(router.urls)),
]
