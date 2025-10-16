from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.users.models import User, Course, Category
from apps.users.models import Lesson, Review


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class ReViewModelSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def rating_validate(self, value):
        if not 1 <= value <= 5:
            raise ValidationError(" siz faqat 1 dan 5 gacha baholay olasiz")
        return value


class CourseModelSerializer(ModelSerializer):
    instructor = HiddenField(default=CurrentUserDefault())
    student_count = IntegerField( read_only=True)
    lesson_count = IntegerField( read_only=True)
    lesson = LessonModelSerializer(read_only=True, many=True)
    review = ReViewModelSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['student_count', 'instructor', 'price', 'category', 'image', 'title', 'lesson_count',
                  'lesson', 'review', 'level'
                  ]

# class FAQSerializer(ModelSerializer):
#     created_by = StringRelatedField(read_only=True)
#
#     class Meta:
#         model = FAQ
#         fields = ['id', 'question', 'answer', 'created_by', 'status', 'created_at', 'answered_at']
