import uuid

from django.contrib.auth import authenticate
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from shared.paginations import CustomPageNumberPagination
from shared.permissions import (
    IsAdminUser,
    IsInstructorOrAdmin,
    IsOwnerOrAdmin,
    IsStudent,
    IsStudentOrAdmin,
)
from users.models import (
    FAQ,
    AuthToken,
    Blog,
    Category,
    Comment,
    Course,
    Device,
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
    LogoutSerializer,
    PaymentModelSerializer,
    RegisterSerializer,
    ReviewModelSerializer,
    SettingModelSerializer,
    TagModelSerializer,
    UserModelSerializer,
    VerifyCodeSerializer,
)
from users.utils import check_verification_code, send_verification_code


@extend_schema(tags=['users'])
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = []

    # pagination_class = CustomPageNumberPagination

    def get_permissions(self):
        if self.action in ['retrieve', 'update']:
            permission_classes = [IsOwnerOrAdmin]
        elif self.action in ['list', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_paginator(self):
        if getattr(self, '_paginator', None) is not None:
            return self._paginator

        if self.action == 'list':
            self._paginator = CustomPageNumberPagination()
        else:
            self._paginator = None

        return self._paginator

    # def get_pagination_classes (self, data):
    #     if self.action == 'list':
    #         return CustomPageNumberPagination
    #     return None


@extend_schema(tags=["Category"])
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
    pagination_class = CustomPageNumberPagination


@extend_schema_view(
    list=extend_schema(description="Get all users(Admin only)", summary="Admin"),
    create=extend_schema(description="Create category (admin only)", summary="Admin"),
    update=extend_schema(description="Update category (admin only)", summary="Admin"),
    partial_update=extend_schema(description="Partial update category (admin only)", summary="Admin"),
    destroy=extend_schema(description="Delete category (admin only)", summary="Admin"),
)
@extend_schema(tags=["Category"])
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUser, ]


# @extend_schema(tags=["Category"])
# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategoryModelSerializer
#     permission_classes = [IsAdminUser]


@extend_schema(tags=["Course"])
class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.select_related('category')
    serializer_class = CourseModelSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsInstructorOrAdmin]
        elif self.action == 'update':
            self.permission_classes = [IsInstructorOrAdmin]
        elif self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]

    @action(methods=['get'], detail=False, url_path='sections', serializer_class=CourseSectionModelSerializer,
            queryset=Section.objects.all())
    def course_sections(self, request):
        qs = self.get_queryset()
        queryset = self.filter_queryset(qs)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


@extend_schema(tags=["Lesson"])
class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.select_related("section__course__category").order_by('section__order_num')
    serializer_class = LessonModelSerializer

    def get_permissions(self):
        if self.action == 'create':
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
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=["Review"])
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer

    def get_permissions(self):
        if self.action == 'create':
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
    permission_classes = [IsStudentOrAdmin, ]
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=["Enrollment & Payment"])
class EnrollmentDestroyAPIView(DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentModelSerializer
    permission_classes = [IsStudentOrAdmin, ]


@extend_schema(tags=["Enrollment & Payment"])
class PaymentCreateListAPIView(ListAPIView, CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
    permission_classes = [IsStudentOrAdmin, ]
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=["Settings & FAQ"])
class FaqListAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FaqModelSerializer
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=["Settings & FAQ"])
class SettingsListAPIView(ListAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingModelSerializer
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=["Tag"])
class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=["Blogs"])
class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsInstructorOrAdmin]
        return [permission() for permission in self.permission_classes]


@extend_schema(tags=["Comments"])
class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.select_related('user', 'blog')
    serializer_class = CommentNestedSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.request.method == 'post':
            return CommentCreateSerializer
        return super().get_serializer_class()


@extend_schema(tags=["Comments"])
class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.select_related('user', 'blog')
    serializer_class = CommentNestedSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


# Register
class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        cache.set(f"tmp_password:{email}", password, timeout=10 * 60)
        try:
            send_verification_code(email)
        except ValidationError as e:
            return Response({"message": str(e)}, status=400)

        return Response({"message": "Verification code sent"}, status=status.HTTP_201_CREATED)


# Verify code
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
            defaults={'is_active': True}
        )

        if created:
            tmp_password = cache.get(f"tmp_password:{email}")
            if not tmp_password:
                return Response({"message": "Password not found. Retry registration"}, status=400)
            user.set_password(tmp_password)
            user.save()
            cache.delete(f"tmp_password:{email}")
        else:
            if not user.is_active:
                user.is_active = True
                user.save()

        return Response({
            "message": "Email verified successfully",
            "email": user.email
        }, status=200)


# Login
class CustomLoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=email, password=password)
        if not user:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        device_id = request.data.get("device_id") or str(uuid.uuid4())
        device_type = request.data.get("device_type", "web")
        agent = request.META.get("HTTP_USER_AGENT", "")

        device_obj, _ = Device.objects.get_or_create(
            device_id=device_id,
            defaults={"type": device_type, "agent": agent}
        )

        token = AuthToken.objects.create(user=user, device=device_obj)

        return Response({
            "token": token.key,
            "user": {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name
            },
            "device": {
                "id": device_obj.id,
                "type": device_obj.type,
                "agent": device_obj.agent
            }
        })


class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    @extend_schema(request=LogoutSerializer)
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device_id = serializer.validated_data["device_id"]

        device = get_object_or_404(Device, device_id=device_id, user=request.user)

        # device.token mavjudligini tekshirish
        if hasattr(device, 'token') and device.token:
            device.token.delete()
            device.token = None
            device.save()

        return Response({"detail": "Logged out successfully"})


@extend_schema(tags=["Get me"])
class UserProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    http_method_names = ['get', 'put']
    permission_classes = [IsAuthenticated, ]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['email']

    def get_object(self):
        return self.request.user
