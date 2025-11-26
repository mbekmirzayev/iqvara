from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.fields import (
    CharField,
    CurrentUserDefault,
    EmailField,
    HiddenField,
    IntegerField,
)
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import FAQ, Category, Course, Device, Lesson, Payment, Review, Setting, Tag, User
from users.models.blogs import Blog, Comment, Step
from users.models.courses import Enrollment, Section


class SafeUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "image",
            "role",
            "date_joined",
        ]


# course.py
class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CourseModelSerializer(ModelSerializer):
    category = CategoryModelSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['title', 'price', 'category', 'lesson_count', 'image']


class CourseSectionModelSerializer(ModelSerializer):
    course = CourseModelSerializer(read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'order_num', 'course']


class LessonModelSerializer(ModelSerializer):
    section = CourseSectionModelSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ["id", "title", "video_url", "duration", "lesson_status", "section"]


class ReViewModelSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewModelSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'student', 'course', 'comment', 'video_comment']


# users.py
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MinimalUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "role", "image"]


# payment.py
class PaymentModelSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def validate(self, data):
        if data.get("payment_type") == "installment":
            if not data.get("installment_months"):
                raise ValidationError({"installment_months": "Required for installment payments"})
            if not data.get("initial_payment_percent"):
                raise ValidationError({"initial_payment_percent": "Required field"})
            percent = float(data["initial_payment_percent"])
            if not (29 <= percent <= 50):
                raise ValidationError({
                    "initial_payment_percent": "Must be between 29% and 50%"
                })
        else:
            data["installment_months"] = None
            data["initial_payment_percent"] = None
        return data


# setting.py (apps/users/setting.py)
class FaqModelSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']


class SettingModelSerializer(ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'device_id', 'type', 'agent', 'updated_at']


# tags.py
class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'slug', 'title', 'created_at', 'updated_at']


# blogs.py
class BlogModelSerializer(ModelSerializer):
    tags = TagModelSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'tags']


class BlogCommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlogStepModelSerializer(ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"


class MinimalBlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title"]


class CommentNestedSerializer(ModelSerializer):
    user = MinimalUserSerializer(read_only=True)
    blog = MinimalBlogSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'updated_at', 'message', 'user', 'blog']


class CommentCreateSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    blog = PrimaryKeyRelatedField(queryset=Blog.objects.all())

    class Meta:
        model = Comment
        fields = ["id", "message", "user", "blog"]


class EnrollmentModelSerializer(ModelSerializer):
    course = CourseModelSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student_id', 'created_at', 'updated_at', 'status', 'course']


class RegisterSerializer(Serializer):
    email = EmailField(default="bekmirzayevoff@gmail.com")
    first_name = CharField(max_length=50, default="Botir")
    last_name = CharField(max_length=50, default="Botirov")
    password = CharField(write_only=True, default="1")

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email already registered")
        return value


class VerifyCodeSerializer(Serializer):
    email = EmailField(default="bekmirzayevoff@gmail.com")
    code = IntegerField()


class LoginSerializer(Serializer):
    email = EmailField(default="bekmirzayevoff@gmail.com")
    password = CharField(write_only=True, default="1")

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise ValidationError("Invalid email or password")
        if not user.is_active:
            raise ValidationError("Account is not verified")

        attrs['user'] = user
        return attrs


class LogoutSerializer(Serializer):
    device_id = CharField()
