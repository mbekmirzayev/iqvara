from django.urls import include, path
from rest_framework.routers import SimpleRouter

from users.views import (
    BlogModelViewSet,
    CategoryListAPIView,
    CategoryViewSet,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
    CourseModelViewSet,
    CustomLoginAPIView,
    CustomLogoutView,
    EnrollmentCreateListAPIView,
    EnrollmentDestroyAPIView,
    FaqListAPIView,
    LessonViewSet,
    PaymentCreateListAPIView,
    RegisterAPIView,
    ReviewViewSet,
    SettingsListAPIView,
    TagListAPIView,
    UserModelViewSet,
    UserProfileViewSet,
    VerifyCodeAPIView,
)

router = SimpleRouter(trailing_slash=False)

router.register(r'users', UserModelViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'courses', CourseModelViewSet, basename='courses')
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'blogs', BlogModelViewSet, basename='blogs')
router.register(r'userprofile', UserProfileViewSet, basename='get_me')

urlpatterns = [
    path('login', CustomLoginAPIView.as_view(), name='knox_login'),
    path('logout', CustomLogoutView.as_view(), name='knox_logout'),

    # ViewSet larni router orqali ulaymiz
    path('', include(router.urls)),

    # ListAPIView yoki CreateAPIView lar
    path('categories', CategoryListAPIView.as_view(), name='category_list'),

    # # Courses_related
    # path('courses/sections', CourseStepListAPIView.as_view(), name='course_steps'),

    # Enrollment va Payment
    path('enrollments', EnrollmentCreateListAPIView.as_view(), name='enrollment_list_create'),
    path('enrollments/<uuid:pk>', EnrollmentDestroyAPIView.as_view(), name='enrollment_destroy'),
    path('payments', PaymentCreateListAPIView.as_view(), name='payment_list_create'),

    # Leaderboard, FAQ, Tag , Setting
    path('faq', FaqListAPIView.as_view(), name='faq'),
    path('tags', TagListAPIView.as_view(), name='tags'),
    path('setting', SettingsListAPIView.as_view(), name='settings'),
    # Comments
    path('comments', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<uuid:pk>', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),

    # Auth (Send / Verify code)
    path('auth/register', RegisterAPIView.as_view(), name='send_code'),
    path('auth/verify_code', VerifyCodeAPIView.as_view(), name='verify_code'),
]
