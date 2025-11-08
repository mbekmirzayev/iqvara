from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    IntegerField,
    TextChoices,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from shared.models import CreateBaseModel, SlugBaseModel


class Promocode(SlugBaseModel, CreateBaseModel):
    title = CharField(max_length=20, verbose_name=_("Title"))
    amount = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    expiry_date = DateTimeField(max_length=5, verbose_name=_("Expiry date"))

    def __str__(self):
        return f"{self.title} ({self.amount})"

    def is_valid(self):
        return self.expiry_date > timezone.now()


class Payment(SlugBaseModel, CreateBaseModel):
    class PaymentType(TextChoices):
        ONE_TIME = 'one_time', _("One time payment")
        Multiple = 'multiple', _("Multiple")  # Multiple

    class CardType(TextChoices):
        UZCARD = 'uzcard', _("Uzcard")
        HUMO = 'humo', _("Humo")

    course_name = CharField(max_length=255, verbose_name=_("Course name"))
    instructor_name = CharField(max_length=255, verbose_name=_("Instructor name"))
    course_price = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Course price"))
    discount = DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Discount"))
    promo_code = ForeignKey('users.Promocode', CASCADE, related_name='promo_code', blank=True, null=True,
                            verbose_name=_("Promo code"))
    payment_type = CharField(max_length=20, choices=PaymentType.choices, default=PaymentType.ONE_TIME,
                             verbose_name=_("Payment type"), )
    installment_months = IntegerField(choices=[(3, "3 months"), (6, "6 months")], blank=True, null=True,
                                      verbose_name=_("Installment period"), )
    initial_payment_percent = DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                           validators=[MinValueValidator(29.0), MaxValueValidator(50.0)], default=29,
                                           verbose_name=_("Initial payment percent"), )
    card_type = CharField(max_length=10, choices=CardType.choices, verbose_name=_("Card type"))
    card_number = CharField(max_length=16, validators=[RegexValidator(r'^\d{16}$', _("Card number is invalid"))],
                            verbose_name=_("Card number"), )
    card_expiry = CharField(max_length=5, verbose_name=_("Expiry date (MM/YY)"))
    phone_number = CharField(max_length=13, validators=[RegexValidator(r'^\+998\d{9}$', _("Phone number is invalid"))],
                             verbose_name=_("Phone number"), )
    total_amount = DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total amount"))

    def clean(self):
        if self.payment_type == self.PaymentType.Multiple:
            if not self.installment_months:
                raise ValidationError(_("Installment period is required for installment payments."))
            if not self.initial_payment_percent:
                raise ValidationError(_("Initial payment percent is required."))
        else:
            self.installment_months = None
            self.initial_payment_percent = None

    def save(self, *args, **kwargs):
        total = self.course_price - self.discount

        if self.promo_code and self.promo_code.is_valid():
            total -= self.promo_code.amount

        if total < 0:
            total = 0

        self.total_amount = total
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course_name} — {self.get_payment_type_display()} — {self.total_amount} UZS"
