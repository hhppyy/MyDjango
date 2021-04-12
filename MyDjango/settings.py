"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)#E:\MyDjango
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+@(c5k=wieekr+po(vw@5)&&!q=(vvptw^k%6y*g4+his-+6j-'

# SECURITY WARNING: don't run with debug turned on in production!

# 由于处于开发阶段，DEBUG 默认为True，当开发完成正式发布产品上线时，需要将DEBUG = False
# ALLOWED_HOSTS是域名访问权限，设置可以访问的域名，默认值为空[], 只允许localhost或127.0.0.1在浏览器上访问。
# DEBUG 改成False之后，需要重新启动服务，同时需要加个ALLOWED_HOSTS 地址，如果想让所以的域名都能访问，可以设置为：ALLOWED_HOSTS = ["*"]

# DEBUG = False
#
# ALLOWED_HOSTS = ['*']

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',          #管理站点
    'django.contrib.auth',           #认证系统
    'django.contrib.contenttypes',   #用于 内容类型的框架
    'django.contrib.sessions',       #会话框架
    'django.contrib.messages',       #消息框架
    'django.contrib.staticfiles',    #管理静态文件框架
    'MyApp',                         #应用APP
    'xadmin',                        # 新添加配置xadmin
    'crispy_forms',                  # 新添加配置xadmin
    'rest_framework',                #restful API
]

#中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'MyDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

"""
settings.py 文件中找到 DATABASES 配置项, django默认连接sqllite。
ENGINE：是指连接数据库驱动的名称,有以下几种情况：

django.db.backends.postgresql 连接 PostgreSQL
django.db.backends.mysql 连接 mysql
django.db.backends.sqlite3 连接 sqlite
django.db.backends.oracle 连接 oracle
"""


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'my_django1',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '123.56.231.107',
        'PORT': '3309',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'  #设置简体中文

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai' #设置中国时区

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False              #设置为False ,要不时间和数据库时间不一致


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# authenticate不会检测用户活跃状态
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']


# session 设置
SESSION_COOLIE_NAME = "key"                # session的cookie保存在浏览器上的可以
SESSION_COOKIE_PATH = "/"                  # session的cookie保存路径（默认）
SESSION_COOKIE_DOMAIN = None               # session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False              # 是否https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True             # 是否session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600               # session的cookie失效时间（2周）（数字为秒）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = True     # 是否关闭浏览器使得session过期（默认）
SESSION_SAVE_EVERY_REQUEST = True          #是否每次请求都保存session，默认修改之后才保存（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True 和
# SESSION_SAVE_EVERY_REQUEST = True 需同时设置否则会导致过期时间无法生效

# 配置上传文件的目录地址
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 配置邮箱

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_SSL = True                   # SSL加密方式
EMAIL_HOST = 'smtp.qq.com'             # 发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 465                       # SMTP服务器端口
EMAIL_HOST_USER = '741841851@qq.com'   # 发件人
EMAIL_HOST_PASSWORD = 'krmhxqxlhuumbbgd'   # 密码(这里使用的是授权码)
EMAIL_FROM = '741841851<741841851@qq.com>'  # 邮件显示的发件人

# 如果是其它的企业邮箱，直接密码登录的话，使用TLS方式
# EMAIL_USE_SSL 和 EMAIL_USE_TLS 是互斥的，只能有一个为 True。

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.xx.com'  # 如果是其它企业邮箱
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'xxx@xx.com' # 帐号
# EMAIL_HOST_PASSWORD = '**********'  # 密码
# EMAIL_FROM = '741841851<xx@xx.com>'   # 邮件显示的发件人








