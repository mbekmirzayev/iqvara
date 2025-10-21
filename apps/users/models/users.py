from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import CharField, ImageField, TextChoices
from django.utils.translation.trans_null import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role='student', **extra_fields):
        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username, email, password, role='admin', **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class  User(AbstractUser):
    class Status(TextChoices):
        ADMIN = 'admin', _('Admin')
        MANAGER = 'manager', _('Manager')
        INSTRUCTOR = 'instructor', _('Instructor')
        STUDENT = 'student', _('Student')

    role = CharField(max_length=20, choices=Status.choices, default=Status.STUDENT)
    phone = CharField(max_length=20, blank=True, null=True)
    image = ImageField(upload_to='users/', null=True, blank=True)

    objects = UserManager()

    def is_admin(self):
        return self.role == self.Status.ADMIN or self.is_superuser

    def is_manager(self):
        return self.role == self.Status.MANAGER

    def is_instructor(self):
        return self.role == self.Status.INSTRUCTOR

    def is_student(self):
        return self.role == self.Status.STUDENT

    def __str__(self):
        return f"{self.username} ({self.role})"
