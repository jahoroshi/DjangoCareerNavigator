from django.contrib import admin
from .models import Skill, JobVac, JobRequiredSkill

admin.site.register(Skill)
admin.site.register(JobVac)
admin.site.register(JobRequiredSkill)
