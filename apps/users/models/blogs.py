from django.db.models import ImageField, ManyToManyField, CASCADE, ForeignKey, CharField, TextField, BooleanField, \
    IntegerField, PositiveIntegerField, DateTimeField
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from shared.models import UUIDBaseModel, SlugBaseModel, CreateBaseModel


class Blog(UUIDBaseModel, SlugBaseModel, CreateBaseModel):
    content = CKEditor5Field()
    is_published = BooleanField(default=False)
    title = CharField(max_length=255)
    image = ImageField(upload_to="blogs/", null=True, blank=True)
    category = ManyToManyField('users.Category', related_name='blogs')
    tags = ManyToManyField('users.Tag', related_name='blogs', blank=True)

    class Meta:
        ordering = _('-created_at',)
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title

    def publish(self):
        self.is_published = True
        self.save()


class Comment(UUIDBaseModel, CreateBaseModel):
    user = ForeignKey('users.User', CASCADE, )
    message = CharField(max_length=100, )
    blog = ForeignKey('users.Blog', CASCADE, related_name='comments')

    class Meta:
        ordering = _('-created_at',)
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f"{self.user},{self.message[:20]}"


class Step(UUIDBaseModel, CreateBaseModel):
    title = CharField(max_length=255)
    content = TextField(null=True, blank=True)
    blog = ForeignKey('users.Blog', CASCADE, related_name='steps', )

    def __str__(self):
        return f"{self.title}, {self.blog}"


class Leaderboard(UUIDBaseModel, CreateBaseModel):
    courses = ManyToManyField('users.Course', related_name='leaderboards')
    user = ForeignKey('users.User', CASCADE, limit_choices_to={'role': 'student'}, related_name='leaderboards')
    points = IntegerField(default=0)
    rank = PositiveIntegerField(default=0, null=True, blank=True)
    date_joined = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user},{self.rank}"
