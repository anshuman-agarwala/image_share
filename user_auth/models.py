from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email

class AppUser(AbstractUser):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    email = models.EmailField(
        unique=True,
        validators=[validate_email],
        blank=False,
        error_messages={
            'unique': 'A user with that email already exists.'
        })
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'