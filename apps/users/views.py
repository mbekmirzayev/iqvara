import random

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from knox.models import AuthToken
from knox.views import LogoutAllView, LogoutView
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from shared.permissions import (
    IsAdminUser,
    IsInstructorOrAdmin,
    IsOwnerOrAdmin,
    IsStudent,
    IsStudentOrAdmin,
)
from users.models import (
    FAQ,
    Blog,
    Category,
    Comment,
    Course,
    Section,
    Enrollment,
    Leaderboard,
    Lesson,
    Payment,
    Review,
    Setting,
    Tag,
    User,
)
from users.serializers import (
    BlogModelSerializer,
    CategoryModelSerializer,
    CommentSerializer,
    CourseModelSerializer,
    CourseStepModelSerializer,
    EnrollmentModelSerializer,
    FaqModelSerializer,
    LeaderBoardModelSerializer,
    LessonModelSerializer,
    PaymentModelSerializer,
    RegisterSerializer,
    SettingModelSerializer,
    TagModelSerializer,
    UserModelSerializer,
    VerifyCodeSerializer, LoginSerializer,
)
from users.utils import send_code

OTP_STORAGE = {}


@extend_schema(tags=['users'])
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = []

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsOwnerOrAdmin]
        elif self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'update':
            permission_classes = [IsOwnerOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


@extend_schema(tags=['users'])
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=["Category"])
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
    permission_classes = [AllowAny]


@extend_schema(tags=["Category"])
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['post', 'put', 'patch', 'delete']


@extend_schema(tags=["Course "])
class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.select_related('instructor', 'category')
    serializer_class = CourseModelSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsInstructorOrAdmin]
        elif self.action == 'update':
            permission_classes = [IsInstructorOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


@extend_schema(tags=["Lesson"])
class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsInstructorOrAdmin]
        elif self.action == 'update':
            permission_classes = [IsInstructorOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


@extend_schema(tags=["Course "])
class CourseStepListAPIView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = CourseStepModelSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=["Review"])
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsStudent]
        elif self.action in ['update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


@extend_schema(tags=["Enrollment & Payment"])
class EnrollmentCreateListAPIView(ListAPIView, CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentModelSerializer
    permission_classes = [IsStudent]


@extend_schema(tags=["Enrollment & Payment"])
class EnrollmentDestroyAPIView(DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentModelSerializer
    permission_classes = [IsStudentOrAdmin]


@extend_schema(tags=["Enrollment & Payment"])
class PaymentCreateListAPIView(ListAPIView, CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
    permission_classes = [IsStudentOrAdmin]


@extend_schema(tags=["LeaderBoard"])
class LeaderBoardListAPIView(ListAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderBoardModelSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=["Settings & FAQ"])
class FaqListAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FaqModelSerializer
    permission_classes = [AllowAny]

    QuerySet = FAQ.objects.all()


@extend_schema(tags=["Settings & FAQ"])
class SettingsListAPIView(ListAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingModelSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=["Tag"])
class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=["Blogs"])
class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'update', 'destroy']:
            return [IsAuthenticated(), IsInstructorOrAdmin()]
        return [AllowAny(), ]


@extend_schema(tags=["Comments"])
class CommentCreateListAPIView(ListAPIView, CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Auth"])
class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user, created = User.objects.get_or_create(
            email=data['email'],
            defaults={
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'is_active': False
            }
        )
        user.set_password(data['password'])
        user.save()

        code = random.randint(100000, 999999)
        send_code(user.email, code)

        return Response({"message": "Code sent to email"}, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Auth"])
class VerifyCodeAPIView(APIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        user.is_active = True
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "id": str(user.id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }, status=status.HTTP_200_OK)


@extend_schema(tags=["Get me"])
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    http_method_names = ['get', 'put']
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['email']

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.request.user


class CustomLoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Tokenlarni tekshirish (maksimal 3)
        tokens = AuthToken.objects.filter(user=user)
        if tokens.count() >= 3:
            # Eng eski tokenni o'chirish
            tokens.order_by('created').first().delete()

        # Yangi token yaratish
        token_instance, token = AuthToken.objects.create(user)
        return Response({
            "user_id": user.id,
            "email": user.email,
            "token": token
        }, status=status.HTTP_200_OK)


class CustomLogoutView(LogoutView):
    pass  # Hozirgi tokenni o'chiradi


class CustomLogoutAllView(LogoutAllView):
    pass  # Foydalanuvchining barcha tokenlarini o'chiradi
