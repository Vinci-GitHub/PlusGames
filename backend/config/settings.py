import os

# 日付・時刻操作モジュール
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7d5_*c#y2@62uf4ly=tbv(o+wodus@%t!^0-pl1i=k$^95xh7d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'rest_framework',
    'djoser',
    'corsheaders',
    # My applications
    'accounts.apps.AccountsConfig',
    'products.apps.ProductsConfig',
    'orders.apps.OrdersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django cors headersを読み込み
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'config.urls'

# BASE_DIR.parent / 'frontend' / 'templates'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Authentication
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'rest_framework:login'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# # # Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# # STATICFILES_DIRS = (
# #     # webpack がここにバンドルしたファイルを吐き出すように設定済み
# #     BASE_DIR.parent / 'frontend' / 'dist',
# # )
# STATIC_ROOT = BASE_DIR / 'static'

#################################################
# REST Framework
#################################################
# REST_FRAMEWORK = {
#     'PAGE_SIZE': 4,
#     'DEFAULT_PAGINATION_CLASS':
#         'rest_framework.pagination.PageNumberPagination',
    # アクセス許可を判断するクラスを指定します。views.py の処理を実行する際に判断します
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 認証に使うクラスを指定します
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',

    # ),
    # 'NON_FIELD_ERRORS_KEY': 'detail',
    # 'TEST_REQUEST_DEFAULT_FORMAT': 'json'
# }

# SIMPLE_JWT = {
#     # トークンをJWTに設定
#     'AUTH_HEADER_TYPES': ('JWT',),
#     # トークンの持続時間の設定
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60)
# }


# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST =(
#     'http://localhost:8080',
#     'http://127.0.0.1:8080',
# )


AUTH_USER_MODEL = 'accounts.CustomUser'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# CORSの設定
# すべて許可
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL = True