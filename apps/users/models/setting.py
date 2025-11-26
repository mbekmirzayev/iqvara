from django.db.models import (
    CASCADE,
    CharField,
    EmailField,
    FloatField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
)
from django.db.models.enums import TextChoices
from django_ckeditor_5.fields import CKEditor5Field
from rest_framework.authtoken.models import Token

from apps.shared.models import CreateBaseModel


class Setting(Model):
    longitude = FloatField(null=True)
    latitude = FloatField(null=True)
    about_us = CKEditor5Field()  # ckeditor5
    phone = CharField(max_length=25)
    contact_email = EmailField()
    support_email = EmailField()
    address = TextField()

    def __str__(self):
        return f"Setting ({self.contact_email})"


class FAQ(CreateBaseModel):
    question = TextField()
    answer = TextField()

    def __str__(self):
        return f"FAQ ({self.question[:20]} , {self.answer[:20]})"


class Device(CreateBaseModel):
    class DeviceType(TextChoices):
        WEB = 'web', 'WEB'
        MOBILE = 'mobile', 'MOBILE'
    device_id = CharField(max_length=255, unique=True)
    type = CharField(max_length=20, choices=DeviceType.choices)
    agent = TextField()
    user = ManyToManyField('users.User', related_name='devices')

    def __str__(self):
        return f"Device({self.device_id} - {self.type})"


class AuthToken(Token):
    user = ForeignKey('users.User', CASCADE)
    device = ForeignKey('users.Device', CASCADE, related_name='auth_token')

    def __str__(self):
        return f"AuthToken ({self.user})"
