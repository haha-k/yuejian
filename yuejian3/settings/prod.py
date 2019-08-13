from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']
print("kkkkkkkk")

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'yuejian3',
        'USER':'root',
        'PASSWORD':'',
        'HOST': 'db',
        'POST':'3306',
        'OPTIONS': {
            'autocommit': True,
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),    #也可以设置seconds=20
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=30),    #也可以设置seconds=20
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
