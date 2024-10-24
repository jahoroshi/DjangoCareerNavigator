from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.candidate.views import CandidateProfileViewSet, CandidateSkillViewSet

router = DefaultRouter()
router.register(r'profile', CandidateProfileViewSet, basename='candidate-profile')
router.register(r'skill', CandidateSkillViewSet, basename='candidate-skill')

urlpatterns = [
    path('', include(router.urls)),
]
