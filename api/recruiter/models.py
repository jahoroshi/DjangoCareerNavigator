from django.db import models
from django.contrib.auth.models import User

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField(blank=True, null=True)
    contact_person = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return self.company_name
