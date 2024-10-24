from rest_framework import serializers
from api.job.models import Skill, JobVac, JobRequiredSkill
from api.recruiter.models import RecruiterProfile

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')

class JobRequiredSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = JobRequiredSkill
        fields = ('id', 'job', 'skill', 'minimal_level', 'minimal_years_experience')

    def create(self, validated_data):
        skill_data = validated_data.pop('skill')
        skill, created = Skill.objects.get_or_create(name=skill_data['name'])
        job_required_skill = JobRequiredSkill.objects.create(skill=skill, **validated_data)
        return job_required_skill


class JobVacSerializer(serializers.ModelSerializer):
    recruiter = serializers.ReadOnlyField(source='recruiter.id')
    requirements = JobRequiredSkillSerializer(source='required_skills', many=True, read_only=True)

    class Meta:
        model = JobVac
        fields = ('id', 'recruiter', 'title', 'description', 'created_at', 'requirements')

    def create(self, validated_data):
        recruiter = self.context['request'].user.recruiterprofile
        job_opening = JobVac.objects.create(recruiter=recruiter, **validated_data)
        return job_opening
