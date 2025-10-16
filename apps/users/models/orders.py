from django.db.models import ForeignKey, CASCADE, CharField, PositiveIntegerField
from django.db.models.enums import TextChoices
from django.utils.translation import gettext_lazy as _
from apps.shared.base import CreateBaseModel, UUIDBaseModel


class Order(CreateBaseModel, UUIDBaseModel):
    amount = PositiveIntegerField(default=0)
    user = ForeignKey('users.User', CASCADE, related_name='orders')
    phone = CharField(verbose_name=_('User Phone'), max_length=20, )

    class OrderStatus(TextChoices):
        DONE = 'done', 'Done'
        REJECTED = 'rejected', 'Rejected'
        PENDING = 'pending', 'Pending'

    order_status = CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    def __str__(self):
        return f"Order {self.id} by {self.user}"

    class Meta:
        ordering = ['-created_at']
