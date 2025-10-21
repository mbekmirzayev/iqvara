from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.users.models import User, Course, Category
from apps.users.models import Lesson, Review
from apps.users.models.payment import Payment
from users.models import FAQ


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
            if not (29 <= percent <=50):
                raise ValidationError({
                    "initial_payment_percent": "Must be between 29% and 50%"
                })
        else:
            data["installment_months"] = None
            data["initial_payment_percent"] = None
        return data


class FaqModelSerializer(ModelSerializer):

    class Meta:
        model = FAQ
        fields = "__all__"