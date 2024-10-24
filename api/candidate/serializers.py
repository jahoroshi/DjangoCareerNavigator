from rest_framework import serializers
from django.contrib.auth.models import User
from api.candidate.models import CandidateProfile, CandidateSkill
from api.job.models import Skill
from api.job.serializers import SkillSerializer
from api.recruiter.serializers import UserSerializer


class CandidateProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CandidateProfile
        fields = ('user', 'full_name', 'contact_email', 'contact_phone', 'resume')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        candidate_profile = CandidateProfile.objects.create(user=user, **validated_data)
        return candidate_profile

    def update(self, instance, validated_data):

        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user_serializer = UserSerializer(instance=user, data=user_data)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
            else:
                raise serializers.ValidationError(user_serializer.errors)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CandidateSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = CandidateSkill
        fields = ('id', 'skill', 'level', 'years_of_experience', 'last_used_year')


    def create(self, validated_data):
        skill_data = validated_data.pop('skill')
        skill, created = Skill.objects.get_or_create(name=skill_data['name'])
        candidate = validated_data.pop('candidate')
        skill_name = skill_data.get('name')

        if CandidateSkill.objects.filter(candidate=candidate, skill__name=skill_name).exists():
            raise serializers.ValidationError(f"У вас уже есть '{skill_name}'.")
        candidate_skill = CandidateSkill.objects.create(candidate=candidate, skill=skill, **validated_data)
        return candidate_skill

    def update(self, instance, validated_data):
        skill_data = validated_data.pop('skill', None)
        candidate = self.context.get('candidate')

        if skill_data:
            skill_name = skill_data.get('name')

            if CandidateSkill.objects.filter(candidate=candidate, skill__name=skill_name).exclude(
                    pk=instance.pk).exists():
                raise serializers.ValidationError(f"У вас уже есть '{skill_name}'.")

            skill, created = Skill.objects.get_or_create(name=skill_name)
            instance.skill = skill

        instance.level = validated_data.get('level', instance.level)
        instance.years_of_experience = validated_data.get('years_of_experience', instance.years_of_experience)
        instance.last_used_year = validated_data.get('last_used_year', instance.last_used_year)

        instance.save()
        return instance


