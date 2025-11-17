from django.db.models import CharField, EmailField, FloatField, Model, TextField
from django_ckeditor_5.fields import CKEditor5Field

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
    device_id = CharField(max_length=255)

    def __str__(self):
        return f"Device ({self.device_id})"
