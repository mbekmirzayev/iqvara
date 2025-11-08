from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from shared.models import CreateBaseModel, SlugBaseModel


class Tag(SlugBaseModel, CreateBaseModel):
    title = CharField(max_length=20)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.title
