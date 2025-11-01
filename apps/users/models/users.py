from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import CharField, ImageField, EmailField, TextChoices
from django.utils.translation import gettext_lazy as _  # to‘g‘risi shu

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

    username = None  # 🔥 username fieldni olib tashladik
    email = EmailField(unique=True)
    role = CharField(max_length=20, choices=Status.choices, default=Status.STUDENT)
    phone = CharField(max_length=20, blank=True, null=True)
    image = ImageField(upload_to='users/', null=True, blank=True)

    USERNAME_FIELD = 'email'       # 🔥 email orqali login
    REQUIRED_FIELDS = []           # superuser yaratishda boshqa fieldlar shart emas

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"

    # Rollar uchun helper funksiyalar
    def is_admin(self):
        return self.role == self.Status.ADMIN or self.is_superuser

    def is_manager(self):
        return self.role == self.Status.MANAGER

    def is_instructor(self):
        return self.role == self.Status.INSTRUCTOR

    def is_student(self):
        return self.role == self.Status.STUDENT
