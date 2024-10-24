from rest_framework import viewsets, permissions

from config.permissions import IsRecruiter
from api.job.models import Skill, JobVac, JobRequiredSkill
from api.job.serializers import SkillSerializer, JobVacSerializer, JobRequiredSkillSerializer
from api.recruiter.models import RecruiterProfile


class JobVacViewSet(viewsets.ModelViewSet):
    serializer_class = JobVacSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return JobVac.objects.none()
        recruiter = RecruiterProfile.objects.get(user=self.request.user)
        return JobVac.objects.filter(recruiter=recruiter)


class JobRequiredSkillViewSet(viewsets.ModelViewSet):
    serializer_class = JobRequiredSkillSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return JobRequiredSkill.objects.none()
        job_id = self.request.query_params.get('job_id')
        return JobRequiredSkill.objects.filter(job__id=job_id)

