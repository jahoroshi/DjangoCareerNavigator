from django.db import IntegrityError
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from api.recruiter.models import RecruiterProfile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'username': {'validators': []},
        }

    def create(self, validated_data):
        try:
            user = User.objects.create(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                raise ValidationError({'username': 'Пользователь уже существует.'})
            raise e

    def validate_username(self, value):
        user = self.instance
        if user and User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError("Пользователь уже существует.")
        return value





class RecruiterProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = RecruiterProfile
        fields = ('user', 'company_name', 'company_description', 'contact_person', 'contact_email')
        ref_name = 'RecruiterUserSerializer'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        recruiter_profile = RecruiterProfile.objects.create(user=user, **validated_data)
        return recruiter_profile

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

