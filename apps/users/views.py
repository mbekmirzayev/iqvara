from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from shared.permissions import IsInstructorOrAdmin
from users.models import FAQ, Category, Course, User
from users.serializers import UserModelSerializer, CategoryModelSerializer, CourseModelSerializer, FaqModelSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('username',)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
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
