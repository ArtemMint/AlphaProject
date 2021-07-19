from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from database import managers


class AbstractUser(AbstractBaseUser):
    """
    AbstractUser model is a base form other user model
    and contain register/login logic.
    """
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    date_joined = models.DateField(
        verbose_name='date joined',
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name='last login',
        auto_now=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
    )

    objects = managers.CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        abstract = True
        ordering = ('-id',)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class User(AbstractUser):
    """
    Custom User model to register and
    login users in application.
    """
    first_name = models.CharField(
        verbose_name='first name',
        max_length=50,
        default='',
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=50,
        default='',
        blank=True,
    )

    class Meta:
        app_label = 'database'

    def __str__(self):
        return self.email

