"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',
    'blog',
    'users'
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
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (BASE_DIR / 'static',)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'users.User'

NULLABLE = {"blank": True, "null": True}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/users/login/'

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CACHES_ENABLED = os.getenv('CACHES_ENABLED') == 'True'

if CACHES_ENABLED:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': os.getenv('LOCATION'),
        }
    }

COUNTRIES_ONLY = {
    'RU': 'Россия',
    'AU': 'Австралия',
    'AT': 'Австрия',
    'AZ': 'Азербайджан',
    'AL': 'Албания',
    'AO': 'Ангола',
    'AD': 'Андорра',
    'AQ': 'Антарктида',
    'AR': 'Аргентина',
    'AM': 'Арминия',
    'AF': 'Афганистан',
    'BD': 'Бангладеш',
    'BB': 'Барбадос',
    'BY': 'Беларусь',
    'BE': 'Бельгия',
    'BJ': 'Бенин',
    'BM': 'Бермуды',
    'BG': 'Болгария',
    'BO': 'Боливия',
    'BA': 'Босния и Герцеговина',
    'BW': 'Ботсвана',
    'BR': 'Бразилия',
    'BF': 'Буркина Фасо',
    'BI': 'Бурунди',
    'BT': 'Бутан',
    'GB': 'Великобритания',
    'HU': 'Венгрия',
    'VE': 'Венесуэлла',
    'VN': 'Вьетнам',
    'GA': 'Габон',
    'GH': 'Гана',
    'GY': 'Гаяна',
    'GP': 'Гваделупа',
    'GT': 'Гватемала',
    'GN': 'Гвинея',
    'DE': 'Германия',
    'HN': 'Гондурас',
    'GL': 'Гренландия',
    'GR': 'Греция',
    'GE': 'Грузия',
    'DK': 'Дания',
    'DM': 'Доминика',
    'DO': 'Доминиканская Республика',
    'EG': 'Египт',
    'ZM': 'Замбия',
    'ZW': 'Зимбабве',
    'IL': 'Израиль',
    'IN': 'Индия',
    'ID': 'Индонезия',
    'JO': 'Иордания',
    'IQ': 'Ирак',
    'IR': 'Иран',
    'IE': 'Ирландия',
    'IS': 'Исландия',
    'ES': 'Испания',
    'IT': 'Италия',
    'YE': 'Йемен',
    'KZ': 'Казахстан',
    'KH': 'Камбоджия',
    'CM': 'Камерун',
    'CA': 'Канада',
    'QA': 'Катар',
    'KE': 'Кения',
    'CY': 'Кипр',
    'KG': 'Киргизия',
    'CN': 'Китай',
    'CO': 'Колумбия',
    'CG': 'Конго',
    'CR': 'Коста-Рика',
    'CU': 'Куба',
    'KW': 'Кувейт',
    'LV': 'Латвия',
    'LR': 'Либерия',
    'LY': 'Ливия',
    'LI': 'Лихтенштейн',
    'LU': 'Люксембург',
    'MR': 'Мавритания',
    'MG': 'Мадагаскар',
    'MK': 'Македония',
    'MY': 'Малайзия',
    'ML': 'Мали',
    'MV': 'Мальдивы',
    'MT': 'Мальта',
    'MX': 'Мексика',
    'MZ': 'Мозамбик',
    'MD': 'Молдовия',
    'MC': 'Монако',
    'MN': 'Монголия',
    'ME': 'Монтенегро',
    'MA': 'Морокко',
    'MM': 'Мьянмар',
    'NA': 'Намибия',
    'NP': 'Непал',
    'NE': 'Нигер',
    'NG': 'Нигерия',
    'NL': 'Нидерланды',
    'NI': 'Никарагуа',
    'NZ': 'Новая Зеландия',
    'NO': 'Норвегия',
    'AE': 'ОАЭ',
    'OM': 'Оман',
    'CX': 'Остров Рождества',
    'PK': 'Пакистан',
    'PW': 'Палау',
    'PS': 'Палестина',
    'PA': 'Панама',
    'PG': 'Папуа Новая Гвинея',
    'PY': 'Парагвай',
    'PE': 'Перу',
    'PL': 'Польша',
    'PT': 'Португалия',
    'PR': 'Пуэрто-Рико',
    'RW': 'Руанда',
    'RO': 'Румыния',
    'US': 'США',
    'WS': 'Самоа',
    'SM': 'Сан-Марино',
    'SA': 'Саудовская Аравия',
    'KP': 'Северная Корея',
    'SC': 'Сейшеллы',
    'SN': 'Сенегал',
    'RS': 'Сербия',
    'SG': 'Сингапур',
    'SY': 'Сирия',
    'SK': 'Словакия',
    'SI': 'Словения',
    'SO': 'Сомали',
    'SD': 'Судан',
    'SL': 'Сьерра-Леоне',
    'TJ': 'Таджикистан',
    'TW': 'Тайвань',
    'TH': 'Тайланд',
    'TZ': 'Танзания',
    'TT': 'Тринидад и Табаго',
    'TN': 'Тунис',
    'TM': 'Туркменистан',
    'TR': 'Турция',
    'UG': 'Уганда',
    'UZ': 'Узбекистан',
    'UA': 'Украина',
    'UY': 'Уругвай',
    'FJ': 'Фиджи',
    'PH': 'Филлипины',
    'FI': 'Финляндия',
    'FR': 'Франция',
    'HR': 'Хорватия',
    'TD': 'Чад',
    'CZ': 'Чехия',
    'CL': 'Чили',
    'CH': 'Швейцария',
    'SE': 'Швеция',
    'LK': 'Шри-Ланка',
    'EC': 'Эквадор',
    'EE': 'Эстония',
    'ET': 'Эфиопия',
    'ZA': 'ЮАР',
    'KR': 'Южная Корея',
    'JM': 'Ямайка',
    'JP': 'Япония'
}
