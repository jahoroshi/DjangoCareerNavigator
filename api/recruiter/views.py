from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from config.permissions import IsRecruiter
from api.recruiter.models import RecruiterProfile
from api.recruiter.serializers import RecruiterProfileSerializer

class RecruiterProfileViewSet(viewsets.ModelViewSet):
    serializer_class = RecruiterProfileSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsRecruiter()]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return RecruiterProfile.objects.none()
        return RecruiterProfile.objects.filter(user=self.request.user)

    def get_object(self):
        if not int(self.kwargs['pk']) == self.request.user.id:
            raise NotFound('Переданный user_id не совпадает с авторизованным пользователем.')

        try:
            return RecruiterProfile.objects.get(user=self.request.user)
        except RecruiterProfile.DoesNotExist:
            raise NotFound('Профиль рекрутера не найден.')



