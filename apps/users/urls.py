from django.urls import path

from users.views import UserListView, CategoryListAPIView, CourseModelViewSet

urlpatterns = [

    # path('FAQ/' , FAQListView.as_view() , name='FAQ-list'),
    path('categories', CategoryListAPIView.as_view(), name='course-list'),
    path('users', UserListView.as_view(), name='user-list'),

    path('courses/', CourseModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    path('courses/<uuid:uuid>/', CourseModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='course-detail'),
]

