from django.db.models import DecimalField, ForeignKey, CASCADE, CharField, TextField, ImageField, \
    ManyToManyField, DurationField
from django.db.models.enums import TextChoices
from django.db.models.fields import URLField, IntegerField
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from shared.models import SlugBaseModel, UUIDBaseModel, CreateBaseModel


class Category(SlugBaseModel):
    name = CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    @property
    def get_courses(self):
        return self.courses.all()


class Course(SlugBaseModel):
    category = ForeignKey('users.Category', CASCADE, related_name='courses')
    short_description = CharField(max_length=100, )
    full_description = CKEditor5Field()
    title = CharField(max_length=255, verbose_name=_("Course title"))
    students = ManyToManyField('users.User', blank=True, through='users.Enrollment', related_name='enrolled_students')
    image = ImageField(upload_to='courses/')
    instructor = ManyToManyField('users.User', limit_choices_to={"role": "instructor"}, related_name='courses')
    price = DecimalField(max_digits=10, decimal_places=2)
    lesson_count = IntegerField(default=0)
    duration = DurationField()

    @property
    def instructor_images(self):
        return [i.image.url for i in self.instructor.all() if i.image]

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title


class CourseStep(UUIDBaseModel):
    course = ForeignKey('users.Course', CASCADE, related_name='course_steps')
    order_num = IntegerField()
    title = CharField(max_length=255, verbose_name=_("Course step title"))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order_num']


class Lesson(UUIDBaseModel):
    class LessonStatus(TextChoices):
        PRIVATE = "private", _("Private")
        PUBLIC = "public", _("Public")

    step = ForeignKey('users.CourseStep', CASCADE, related_name='lessons')
    title = CharField(max_length=100)
    video_url = URLField()
    lesson_content = CKEditor5Field(blank=True, null=True)  # ?
    duration = DurationField()
    lesson_status = CharField(choices=LessonStatus.choices, default=LessonStatus.PRIVATE)

    def __str__(self):
        return f"{self.title}, {self.step}"


class Enrollment(CreateBaseModel):
    class Status(TextChoices):
        IN_PROGRESS = 'in_progress', _('In Progress')
        COMPLETED = 'completed', _('Completed')

    student = ForeignKey('users.User', CASCADE, limit_choices_to={'role': 'student'})
    course = ForeignKey('users.Course', CASCADE, related_name='enrolments')
    status = CharField(max_length=20, choices=Status.choices, default=Status.IN_PROGRESS)


class Review(CreateBaseModel):
    student = ForeignKey('users.User', CASCADE, related_name='reviews')
    course = ForeignKey('users.Course', CASCADE)
    comment = TextField(null=True, blank=True)
    video_comment = URLField(blank=True, null=True)
