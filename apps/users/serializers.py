from rest_framework.exceptions import ValidationError
from rest_framework.fields import (
    CharField,
    CurrentUserDefault,
    EmailField,
    HiddenField,
    IntegerField,
)
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import FAQ, Category, Course, Lesson, Payment, Review, Setting, Tag, User
from users.models.blogs import Blog, Comment, Leaderboard, Step
from users.models.courses import Section, Enrollment
from users.utils import check_email

from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models import User  # Sendagi User modeli

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            email=data.get('email'),
            password=data.get('password')
        )
        if not user:
            raise serializers.ValidationError("Email yoki parol noto‘g‘ri")
        data['user'] = user
        return data


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
        fields = "__all__"


class LessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class ReViewModelSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CourseModelSerializer(ModelSerializer):
    instructor = HiddenField(default=CurrentUserDefault())
    student_count = IntegerField(read_only=True)
    lesson_count = IntegerField(read_only=True)
    lesson = LessonModelSerializer(read_only=True, many=True)
    review = ReViewModelSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['student_count', 'instructor', 'price', 'category', 'image', 'title', 'lesson_count',
                  'lesson', 'review']


class CourseStepModelSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class ReviewModelSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# users.py
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


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
        fields = "__all__"


class SettingModelSerializer(ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"


# tags.py
class TagModelSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


# blogs.py
class BlogModelSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class LeaderBoardModelSerializer(ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = "__all__"


class BlogCommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlogStepModelSerializer(ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class EnrollmentModelSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"


class RegisterSerializer(Serializer):
    email = EmailField(max_length=50, default='admin@gmail.com')
    first_name = CharField(max_length=50, default='Botir')
    last_name = CharField(max_length=50, default='Tohirov')
    password = CharField(max_length=128, write_only=True, default='1')


class VerifyCodeSerializer(Serializer):
    email = EmailField(default='admin@gmail.com')
    code = IntegerField()
    token_class = RefreshToken

    default_error_messages = {
        "no_active_account": "No active account found with the given credentials"
    }

    def get_data(self):
        refresh = self.get_token(self.user)
        user_data = UserModelSerializer(self.user).data
        tokens = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }
        data = {**tokens, **user_data}
        return data

    def validate(self, attrs):
        email = attrs['email']
        code = attrs['code']

        is_valid = check_email(email, code)
        if not is_valid:
            raise ValidationError({'message': 'Invalid or expired code'})

        self.user, _ = User.objects.get_or_create(email=email)
        attrs['user'] = self.user
        return attrs

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)
