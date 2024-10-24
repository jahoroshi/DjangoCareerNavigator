from api.candidate.models import CandidateProfile, CandidateSkill
from api.job.models import JobVac, JobRequiredSkill
from django.db.models import Q
from datetime import datetime

def get_level_score(candidate_level, required_level):
    levels = {'Beginner': 1, 'Intermediate': 2, 'Advanced': 3}
    return levels.get(candidate_level, 0) - levels.get(required_level, 0)

def get_last_used_score(last_used_year):
    current_year = datetime.now().year
    if current_year - last_used_year <= 2:
        return 1
    return 0

def match_candidates(job_id):
    job = JobVac.objects.get(id=job_id)
    required_skills = JobRequiredSkill.objects.filter(job=job)
    candidates = CandidateProfile.objects.all()
    candidate_scores = []

    for candidate in candidates:
        candidate_skills = CandidateSkill.objects.filter(candidate=candidate)
        score = 0

        for req_skill in required_skills:
            matching_skill = candidate_skills.filter(skill=req_skill.skill).first()
            if matching_skill:
                level_score = get_level_score(matching_skill.level, req_skill.minimal_level)
                exp_score = matching_skill.years_of_experience - req_skill.minimal_years_experience
                last_used_score = get_last_used_score(matching_skill.last_used_year)
                score += level_score + exp_score + last_used_score
            else:
                score -= 1

        candidate_scores.append({'candidate': candidate, 'score': score})

    sorted_candidates = sorted(candidate_scores, key=lambda x: x['score'], reverse=True)
    return [item['candidate'] for item in sorted_candidates]

def match_jobs(candidate_id):
    candidate = CandidateProfile.objects.get(user__id=candidate_id)
    candidate_skills = CandidateSkill.objects.filter(candidate=candidate)
    jobs = JobVac.objects.all()
    job_scores = []

    for job in jobs:
        required_skills = JobRequiredSkill.objects.filter(job=job)
        score = 0

        for req_skill in required_skills:
            matching_skill = candidate_skills.filter(skill=req_skill.skill).first()
            if matching_skill:
                level_score = get_level_score(matching_skill.level, req_skill.minimal_level)
                exp_score = matching_skill.years_of_experience - req_skill.minimal_years_experience
                last_used_score = get_last_used_score(matching_skill.last_used_year)
                score += level_score + exp_score + last_used_score
            else:
                score -= 1

        job_scores.append({'job': job, 'score': score})

    sorted_jobs = sorted(job_scores, key=lambda x: x['score'], reverse=True)
    return [item['job'] for item in sorted_jobs]
