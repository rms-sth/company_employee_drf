from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'is_staff', 'is_active']

    def __str__(self):
        return "{}".format(self.email)


class CompanyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='companyprofile')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{}".format(self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userprofile')
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.company)
