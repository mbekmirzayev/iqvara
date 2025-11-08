from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import CharField, EmailField, ImageField, TextChoices
from django.utils.translation import gettext_lazy as _

from shared.models import UUIDBaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='student', **extra_fields):
        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, role='admin', **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser, UUIDBaseModel):
    class Status(TextChoices):
        ADMIN = 'admin', _('Admin')
        MANAGER = 'manager', _('Manager')
        INSTRUCTOR = 'instructor', _('Instructor')
        STUDENT = 'student', _('Student')

    username = None
    email = EmailField(unique=True)
    role = CharField(max_length=20, choices=Status.choices, default=Status.STUDENT)
    phone = CharField(max_length=20, blank=True, )
    image = ImageField(upload_to='users/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"

    # Rollar uchun helper funksiyalar
    @property
    def is_admin(self):
        return self.role == self.Status.ADMIN or self.is_superuser

    @property
    def is_manager(self):
        return self.role == self.Status.MANAGER

    @property
    def is_instructor(self):
        return self.role == self.Status.INSTRUCTOR

    @property
    def is_student(self):
        return self.role == self.Status.STUDENT
