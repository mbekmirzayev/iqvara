from django.db.models import CharField

from shared.models import SlugBaseModel, CreateBaseModel, UUIDBaseModel
from django.utils.translation import gettext_lazy as _

class Tag(SlugBaseModel, CreateBaseModel , UUIDBaseModel):
    title = CharField(max_length=20)


    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.title
