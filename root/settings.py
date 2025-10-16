import os
from pathlib import Path
from dotenv import load_dotenv

# --- BASE DIR ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- .env ---
load_dotenv(BASE_DIR / '.env')
SECRET_KEY = os.getenv('SECRET_KEY')

# --- DEBUG & HOSTS ---
DEBUG = True
ALLOWED_HOSTS = ['*']

# --- INSTALLED APPS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'apps.users',
    'apps.shared',

    # Third party
    'drf_spectacular',
    'django_filters',
    'django_ckeditor_5',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# --- ROOT URLS ---
ROOT_URLCONF = 'root.urls'
WSGI_APPLICATION = 'root.wsgi.application'

# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend' / 'templates'],  # index.html
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- DATABASE ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_NAME'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
        "USER": os.getenv('POSTGRES_USER'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD')
    }
}

# --- AUTH USER MODEL ---
AUTH_USER_MODEL = 'users.User'

# --- PASSWORD VALIDATORS ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# --- INTERNAL IPs ---
INTERNAL_IPS = ["127.0.0.1", "localhost"]

# --- LANGUAGE & TIMEZONE ---
LANGUAGE_CODE = 'en'
LANGUAGES = [('en', 'English'), ('uz', 'Uzbek')]
LOCALE_PATHS = [BASE_DIR / 'locale']
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',            # global static
    BASE_DIR / 'apps' / 'static',   # apps ichidagi static
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # collectstatic natijasi

# --- MEDIA FILES ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- DEFAULT AUTO FIELD ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- REST FRAMEWORK ---
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,
}

# --- CKEDITOR SETTINGS (soddalashtirilgan) ---
CKEDITOR_5_CONFIGS = {
    'default': {'toolbar': {'items': ['heading', '|', 'bold', 'italic', 'link','bulletedList','numberedList','blockQuote','imageUpload']}},
}

# --- CACHE ---
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# --- DEBUG TOOLBAR ---
if DEBUG:
    INTERNAL_IPS += ['127.0.0.1']

# --- JAZZMIN SETTINGS (optional) ---
JAZZMIN_SETTINGS = {
    "site_title": "My Admin",
    "site_header": "My Admin Panel",
    "welcome_sign": "Welcome to My Custom Admin",
    "site_logo": "apps/images/logo.png",
    "site_logo_classes": "img-circle object-cover",
    "site_logo_height": "12px",
    "login_logo": "images/logo.png",
    "login_logo_height": "60px",
    "language_chooser": True,
}
