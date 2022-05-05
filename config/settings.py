from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-x9fs2#c@5#g2#qx=u8ietno_0e@fr8l!*2etn^75+2dl8symsb'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local
    'music.apps.MusicConfig',
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    #  3rd-party apps
    'bootstrap5',
    "crispy_forms",
    "crispy_bootstrap5",
    'allauth',
    'allauth.account',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'  # Дефолтные настройки теперь будут настраиваемы

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"  # ДЛЯ ФОРМ БУТСТРАПА
CRISPY_TEMPLATE_PACK = "bootstrap5"  # ДЛЯ ФОРМ БУТСТРАПА

# django-allauth config
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'home'
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # автоматически будет отправлять на почту подтверждение при регистрации
# ACCOUNT_SESSION_REMEMBER = True # при выходе пользователя с сайта сохранять ли его сессию?
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True  # нужно ли при регистрации два раза ввести пароль?
ACCOUNT_USERNAME_REQUIRED = True  # нужно ли при регистрации указывать свой логин?
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # имя пользователя или его логин используются для авторизации
ACCOUNT_EMAIL_REQUIRED = True  # Пользователю необходимо указать e-mail при регистрации
ACCOUNT_UNIQUE_EMAIL = True  # Пользователь только с уникальным емайлом может зарегистрироваться
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}
