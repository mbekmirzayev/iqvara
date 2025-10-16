from django.db.models import CharField

from apps.shared.base import SlugBaseModel, CreateBaseModel, UUIDBaseModel


class Tag(SlugBaseModel, CreateBaseModel , UUIDBaseModel):
    title = CharField(max_length=20)


    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title
