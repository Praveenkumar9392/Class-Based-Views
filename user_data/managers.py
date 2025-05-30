from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from accounts.models import *


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if other_fields.get('is_staff') is not True:
            raise ValueError('Staff must have is_staff=True.')

        if other_fields.get('is_active') is not True:
            raise ValueError('Active must have is_active=True.')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide a mobileno'))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user