from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.users.models import Category, Course, User
from apps.shared.permissions import IsInstructorOrAdmin
from apps.users.serializers import UserModelSerializer, CategorySerializer, CourseModelSerializer, FaqModelSerializer
from users.models import FAQ


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('username',)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)


# class
@extend_schema(tags={"Course"})
class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.select_related('instructor', 'category')
    serializer_class = CourseModelSerializer
    permission_classes = [IsInstructorOrAdmin]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('title', 'price',)

class FaqListAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FaqModelSerializer
