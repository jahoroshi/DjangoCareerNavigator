from django.urls import path
from api.matching.views import CandidateMatchingView, JobMatchingView

urlpatterns = [
    path('candidates/<int:job_id>/', CandidateMatchingView.as_view(), name='candidate-matching'),
    path('jobs/<int:candidate_id>/', JobMatchingView.as_view(), name='job-matching'),
]
