from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    qualifications = models.CharField(max_length=255, blank=True)
    short_description = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)


class Service(models.Model):
    service_title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.service_title
