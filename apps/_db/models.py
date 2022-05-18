from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from _db import managers


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
        verbose_name='date_joined',
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name='last_login',
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
        verbose_name='first_name',
        max_length=50,
        default='',
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='last_name',
        max_length=50,
        default='',
        blank=True,
    )
    # user_name = models.CharField(
    #     verbose_name='user_name',
    #     max_length=50,
    #     default='',
    #     blank=True,
    # )

    class Meta:
        app_label = '_db'

    def __str__(self):
        return self.email
