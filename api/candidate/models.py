from django.db import models
from django.contrib.auth.models import User
from api.job.models import Skill

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class CandidateSkill(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Начальный'),
        ('Intermediate', 'Средний'),
        ('Advanced', 'Продвинутый'),
    ]

    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES)
    years_of_experience = models.PositiveIntegerField()
    last_used_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.candidate.full_name} - {self.skill.name}"
