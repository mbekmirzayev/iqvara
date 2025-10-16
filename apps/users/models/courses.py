from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import DecimalField, IntegerField, ForeignKey, CASCADE, CharField, TextField, ImageField, \
    ManyToManyField, DurationField
from django.db.models.enums import TextChoices
from django.db.models.fields import URLField
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from apps.shared.base import SlugBaseModel, UUIDBaseModel, CreateBaseModel


class Category(SlugBaseModel, UUIDBaseModel):
    name = CharField(max_length=100, unique=True)
    description = TextField(blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_courses(self):
        return self.courses.all()


class Course(SlugBaseModel, UUIDBaseModel):
    class CourseLevel(TextChoices):
        BEGINNER = 'beginner', 'Beginner'
        INTERMEDIATE = 'intermediate', 'Intermediate'
        ADVANCED = 'advanced', 'Advanced'

    students = ManyToManyField('users.User', blank=True, related_name='enrolled_students')
    image = ImageField(upload_to='courses/')
    instructor = ForeignKey('users.User', CASCADE, limit_choices_to={"role": "instructor"}, related_name='courses')
    category = ForeignKey('users.Category', CASCADE, related_name='courses')
    title = CharField(max_length=255, verbose_name=_("Course title"))
    description = CKEditor5Field()  # TODO ckeditor5
    price = DecimalField(max_digits=10, decimal_places=2)
    # duration = IntegerField(help_text="Darslar davomiyligi (soatlarda)", editable=False) 23:16
    duration = DurationField()

    level = CharField(max_length=20, choices=CourseLevel.choices)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title


class Lesson(UUIDBaseModel, SlugBaseModel):
    course = ForeignKey('users.Course', CASCADE, related_name='lessons')
    title = CharField(max_length=100, )
    video_url = URLField()
    lesson_content = TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.course}"


class Review(UUIDBaseModel, CreateBaseModel):
    student = ForeignKey('users.User', CASCADE, related_name='reviews')
    course = ForeignKey('users.Course', CASCADE)
    rating = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = TextField(null=True, blank=True)
