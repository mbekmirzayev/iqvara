from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API uchun yo‘llar
    path('api/', include('apps.users.urls')),

    # Frontend sahifasi
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
