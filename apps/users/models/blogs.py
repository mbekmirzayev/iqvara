from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    ImageField,
    IntegerField,
    Manager,
    ManyToManyField,
    PositiveIntegerField,
    QuerySet,
    TextField,
)
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from shared.models import CreateBaseModel, SlugBaseModel


class BlogQuerySet(QuerySet):

    def all(self):
        return self.filter(is_published=True)

    def unpublished(self):
        return self.filter(is_published=False)


class BlogManager(Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)


class Blog(SlugBaseModel, CreateBaseModel):
    content = CKEditor5Field()
    is_published = BooleanField(default=False)
    title = CharField(max_length=255)
    image = ImageField(upload_to="blogs/", null=True, blank=True)
    category = ManyToManyField('users.Category', related_name='blogs')
    tags = ManyToManyField('users.Tag', related_name='blogs', blank=True)
    number_of_views = PositiveIntegerField(default=0)
    read_time = PositiveIntegerField(default=0)

    class Meta:
        ordering = '-created_at',
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title

    def publish(self):
        self.is_published = True
        self.save(update_fields=['is_published'])


class Comment(CreateBaseModel):
    user = ForeignKey('users.User', CASCADE)
    message = CharField(max_length=100)
    blog = ForeignKey('users.Blog', CASCADE, related_name='comments')

    class Meta:
        ordering = '-created_at',
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f"{self.user},{self.message[:20]}"


class Step(CreateBaseModel):
    title = CharField(max_length=255)
    content = TextField(blank=True)
    blog = ForeignKey('users.Blog', CASCADE, related_name='steps', )

    def __str__(self):
        return f"{self.title}, {self.blog}"


class Leaderboard(CreateBaseModel):  # TODO ?
    courses = ManyToManyField('users.Course', related_name='leaderboards')
    user = ForeignKey('users.User', CASCADE, limit_choices_to={'role': 'student'}, related_name='leaderboards')
    points = IntegerField(default=0)
    rank = PositiveIntegerField(default=0, null=True, blank=True)
    date_joined = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user},{self.rank}"
