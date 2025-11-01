from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import (
    UserModelViewSet, UserListAPIView,
    CategoryViewSet, CategoryListAPIView,
    CourseModelViewSet, LessonViewSet, CourseStepListAPIView, ReviewViewSet,
    EnrollmentCreateListAPIView, EnrollmentDestroyAPIView, PaymentCreateListAPIView,
    LeaderBoardListAPIView, FaqListAPIView, TagListAPIView,
    BlogModelViewSet, CommentCreateListAPIView,
    VerifyCodeAPIView, SettingsListAPIView, RegisterAPIView, UserProfileViewSet
)

router = DefaultRouter()

router.register(r'users', UserModelViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'courses', CourseModelViewSet, basename='courses')
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'blogs', BlogModelViewSet, basename='blogs')
router.register(r'userprofile', UserProfileViewSet, basename='get-me')

urlpatterns = [
    # ViewSet larni router orqali ulaymiz
    path('', include(router.urls)),

    # ListAPIView yoki CreateAPIView lar
    path('user-list', UserListAPIView.as_view(), name='user-list'),
    path('category-list', CategoryListAPIView.as_view(), name='category-list'),

    # Courses-related
    path('course-steps', CourseStepListAPIView.as_view(), name='course-steps'),

    # Enrollment va Payment
    path('enrollments', EnrollmentCreateListAPIView.as_view(), name='enrollment-list-create'),
    path('enrollments/<uuid:pk>', EnrollmentDestroyAPIView.as_view(), name='enrollment-destroy'),
    path('payments', PaymentCreateListAPIView.as_view(), name='payment-list-create'),

    # Leaderboard, FAQ, Tag , Setting
    path('leaderboard', LeaderBoardListAPIView.as_view(), name='leaderboard'),
    path('faq', FaqListAPIView.as_view(), name='faq'),
    path('tags', TagListAPIView.as_view(), name='tags'),
    path('setting' ,SettingsListAPIView.as_view(), name='settings'),
    # Comments
    path('comments/', CommentCreateListAPIView.as_view(), name='comment-list-create'),

    # Auth (Send / Verify code)
    path('auth/Register', RegisterAPIView.as_view(), name='send-code'),
    path('auth/Login', VerifyCodeAPIView.as_view(), name='verify-code'),
]
