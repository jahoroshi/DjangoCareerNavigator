# conftest.py
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from api.candidate.models import CandidateProfile, CandidateSkill
from api.recruiter.models import RecruiterProfile
from api.job.models import Skill, JobVac, JobRequiredSkill
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def get_token_for_user(api_client, create_user):
    def make_token(username, password, **kwargs):
        user = create_user(username=username, password=password, **kwargs)
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    return make_token


@pytest.fixture
def authenticated_client(api_client, get_token_for_user):
    def get_client(username='testuser', password='testpass', **kwargs):
        token = get_token_for_user(username, password, **kwargs)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        return api_client
    return get_client


@pytest.fixture
def candidate_user(create_user):
    return create_user(username='candidate', password='candidatepass')


@pytest.fixture
def recruiter_user(create_user):
    return create_user(username='recruiter', password='recruiterpass')


@pytest.fixture
def candidate_profile(candidate_user):
    return CandidateProfile.objects.create(
        user=candidate_user,
        full_name='Candidate User',
        contact_email='candidate@example.com'
    )


@pytest.fixture
def recruiter_profile(recruiter_user):
    return RecruiterProfile.objects.create(
        user=recruiter_user,
        company_name='Example Corp',
        contact_person='Recruiter User',
        contact_email='recruiter@example.com'
    )


@pytest.fixture
def skill():
    return Skill.objects.create(name='Python')


@pytest.fixture
def job_vacancy(recruiter_profile):
    return JobVac.objects.create(
        recruiter=recruiter_profile,
        title='Senior Developer',
        description='Looking for a senior developer.'
    )


@pytest.fixture
def candidate_skill(candidate_profile, skill):
    return CandidateSkill.objects.create(
        candidate=candidate_profile,
        skill=skill,
        level='Advanced',
        years_of_experience=5,
        last_used_year=2021
    )


@pytest.fixture
def job_required_skill(job_vacancy, skill):
    return JobRequiredSkill.objects.create(
        job=job_vacancy,
        skill=skill,
        minimal_level='Intermediate',
        minimal_years_experience=3
    )
