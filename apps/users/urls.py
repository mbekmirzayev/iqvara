from django.urls import include, path
from knox import views as knox_views
from rest_framework.routers import DefaultRouter

from users.views import (
    BlogModelViewSet,
    CategoryListAPIView,
    CategoryViewSet,
    CommentCreateListAPIView,
    CourseModelViewSet,
    CourseStepListAPIView,
    EnrollmentCreateListAPIView,
    EnrollmentDestroyAPIView,
    FaqListAPIView,
    LeaderBoardListAPIView,
    LessonViewSet,
    PaymentCreateListAPIView,
    RegisterAPIView,
    ReviewViewSet,
    SettingsListAPIView,
    TagListAPIView,
    UserListAPIView,
    UserModelViewSet,
    UserProfileViewSet,
    VerifyCodeAPIView, CustomLoginView, CustomLogoutView, CustomLogoutAllView,
)

router = DefaultRouter()

router.register(r'users', UserModelViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'courses', CourseModelViewSet, basename='courses')
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'blogs', BlogModelViewSet, basename='blogs')
router.register(r'userprofile', UserProfileViewSet, basename='get-me')

# urls.py

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='knox_login'),
    path('logout/', CustomLogoutView.as_view(), name='knox_logout'),
    path('logoutall/', CustomLogoutAllView.as_view(), name='knox_logoutall'),

    # ViewSet larni router orqali ulaymiz
    path('', include(router.urls)),

    # ListAPIView yoki CreateAPIView lar
    path('user-list', UserListAPIView.as_view(), name='user-list'),
    path('categories', CategoryListAPIView.as_view(), name='category-list'),

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
    path('setting', SettingsListAPIView.as_view(), name='settings'),
    # Comments
    path('comments/', CommentCreateListAPIView.as_view(), name='comment-list-create'),

    # Auth (Send / Verify code)
    path('auth/register', RegisterAPIView.as_view(), name='send-code'),
    path('auth/login', VerifyCodeAPIView.as_view(), name='verify-code'),
]
