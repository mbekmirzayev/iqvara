from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from knox.views import LogoutAllView, LogoutView
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

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
    Enrollment,
    Lesson,
    Payment,
    Review,
    Section,
    Setting,
    Tag,
    User,
)
from users.serializers import (
    BlogModelSerializer,
    CategoryModelSerializer,
    CommentCreateSerializer,
    CommentNestedSerializer,
    CourseModelSerializer,
    CourseSectionModelSerializer,
    EnrollmentModelSerializer,
    FaqModelSerializer,
    LessonModelSerializer,
    LoginSerializer,
    PaymentModelSerializer,
    RegisterSerializer,
    SettingModelSerializer,
    TagModelSerializer,
    UserModelSerializer,
    VerifyCodeSerializer,
)
from users.utils import check_verification_code, create_user_token, send_verification_code

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
    queryset = Course.objects.select_related('category')
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
    queryset = Lesson.objects.select_related("section__course__category").order_by('section__order_num')
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
    serializer_class = CourseSectionModelSerializer
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
    permission_classes = [IsStudentOrAdmin]


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
class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.select_related('user', 'blog').all()
    serializer_class = CommentNestedSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Comments"])
class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(tags=["Comments"])
class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.select_related('user', 'blog').all()
    serializer_class = CommentNestedSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


# Register
class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        try:
            send_verification_code(email)
        except ValidationError as e:
            return Response({"message": str(e)}, status=400)

        return Response({"message": "Verification code sent"}, status=status.HTTP_201_CREATED)


#  Verify code
class VerifyCodeAPIView(APIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        if not check_verification_code(email, code):
            return Response({"message": "Invalid or expired code"}, status=400)

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'first_name': serializer.validated_data['first_name'],
                'last_name': serializer.validated_data['last_name'],
                'is_active': True
            }
        )
        if created:
            user.set_password(serializer.validated_data['password'])
            user.save()
        else:
            if not user.is_active:
                user.is_active = True
                user.save()

        return Response({
            "message": "Email verified successfully",
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }, status=200)


# Login
class CustomLoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token = create_user_token(user)

        return Response({
            "token": token,
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }, status=200)


# Logout / LogoutAll
class CustomLogoutView(LogoutView):
    pass


class CustomLogoutAllView(LogoutAllView):
    pass


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
