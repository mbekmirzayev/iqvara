from django.db.models import ImageField, ManyToManyField, CASCADE, ForeignKey , CharField, TextField, BooleanField
from django_ckeditor_5.fields import CKEditor5Field

from shared.models import SlugBaseModel, CreateBaseModel, UUIDBaseModel


class Blog(UUIDBaseModel, SlugBaseModel, CreateBaseModel):
    content = CKEditor5Field()
    is_published = BooleanField(default=False)
    title = CharField(max_length=255)
    image = ImageField(upload_to="blogs/", null=True, blank=True)
    category = ManyToManyField('users.Category', related_name='blogs')
    tags = ManyToManyField('users.Tag', related_name='blogs', blank=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'



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
        ordering = ('-created_at',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.user},{self.message[:20]}"


class Step(UUIDBaseModel, CreateBaseModel):
    title = CharField(max_length=255)
    content = TextField(null=True, blank=True)
    blog = ForeignKey('users.Blog', CASCADE, related_name='steps', )

    def __str__(self):
        return f"{self.title}, {self.blog}"
