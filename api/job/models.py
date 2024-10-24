from django.db import models
from api.recruiter.models import RecruiterProfile

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return self.name

class JobVac(models.Model):
    recruiter = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE, related_name='job_openings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobRequiredSkill(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Начальный'),
        ('Intermediate', 'Средний'),
        ('Advanced', 'Продвинутый'),
    ]

    job = models.ForeignKey(JobVac, on_delete=models.CASCADE, related_name='required_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    minimal_level = models.CharField(max_length=12, choices=LEVEL_CHOICES)
    minimal_years_experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.job.title} - {self.skill.name}"
