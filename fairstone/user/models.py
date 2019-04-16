from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models


def get_email_validator(field_name):
    return validators.RegexValidator(
        r'^[\w.@+-]+$',
        'Enter a valid {}. This value may contain only letters, numbers and '
        '@/./+/-/_ characters.'.format(field_name),
    )


class FairstoneUser(AbstractUser):

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    username = models.CharField(
        'username',
        max_length=245,
        unique=True,
        validators=[get_email_validator('username')],
    )
    email = models.EmailField(unique=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ema
