from rest_framework import generics, permissions
from api.candidate.serializers import CandidateProfileSerializer
from api.job.serializers import JobVacSerializer
from config.permissions import IsRecruiter, IsCandidate
from api.matching.utils import match_candidates, match_jobs

class CandidateMatchingView(generics.ListAPIView):
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecruiter]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return match_candidates(job_id)

class JobMatchingView(generics.ListAPIView):
    serializer_class = JobVacSerializer
    permission_classes = [permissions.IsAuthenticated, IsCandidate]

    def get_queryset(self):
        candidate_id = self.kwargs['candidate_id']
        return match_jobs(candidate_id)
