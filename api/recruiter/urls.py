from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.recruiter.views import RecruiterProfileViewSet

router = DefaultRouter()
router.register(r'profile', RecruiterProfileViewSet, basename='recruiter-profile')

urlpatterns = [
    path('', include(router.urls)),
]
