from django.db.models import Model, TextField, CharField, EmailField, FloatField
from django_ckeditor_5.fields import CKEditor5Field

from apps.shared.models import UUIDBaseModel, CreateBaseModel


class Settings(Model):
    longitude = FloatField(null=True)
    latitude = FloatField(null=True)
    about_us = CKEditor5Field()  # ckeditor5
    phone = CharField(max_length=25)
    contact_email = EmailField()
    support_email = EmailField()
    address = TextField()

    def __str__(self):
        return f"Settings ({self.contact_email})"


class FAQ(UUIDBaseModel, CreateBaseModel):
    # class Status(TextChoices):  # TODO ?
    #     PENDING = 'pending', 'Pending'
    #     ANSWERED = 'answered', 'Answered'

    question = TextField()
    answer = TextField()

    # created_by = ForeignKey("users.User", CASCADE, related_name='faqs')
    # status = CharField(max_length=20, choices=Status.choices, default=Status.PENDING)  # TODO ?
    # created_at = DateTimeField(auto_now_add=True)
    # answered_at = DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"FAQ ({self.question[:20]} , {self.answer[:20]})"
