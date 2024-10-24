from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from config.permissions import IsCandidate
from api.candidate.models import CandidateProfile, CandidateSkill
from api.candidate.serializers import CandidateProfileSerializer, CandidateSkillSerializer
from django.contrib.auth.models import User

class CandidateProfileViewSet(viewsets.ModelViewSet):
    # queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsCandidate()]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return CandidateProfile.objects.none()
        return CandidateProfile.objects.filter(user=self.request.user)

    def get_object(self):
        if not int(self.kwargs['pk']) == self.request.user.id:
            raise NotFound('Переданный user_id не совпадает с авторизованным пользователем.')
        try:
            return CandidateProfile.objects.get(user=self.request.user)
        except CandidateProfile.DoesNotExist:
            raise NotFound('Профиль кандидата не найден.')



class CandidateSkillViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSkillSerializer
    permission_classes = [permissions.IsAuthenticated, IsCandidate()]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return CandidateSkill.objects.none()
        candidate = CandidateProfile.objects.get(user=self.request.user)
        return CandidateSkill.objects.filter(candidate=candidate)

    def perform_create(self, serializer):
        candidate = CandidateProfile.objects.get(user=self.request.user)
        serializer.save(candidate=candidate)
