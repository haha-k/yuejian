from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# print("")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 设置数据库为mysql
        'NAME': 'yuejian3',  # 数据库名为alldb
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123',  # 数据库用户密码
        # 'HOST':'db',
        'OPTIONS': {
            'autocommit': True,
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# drf dev
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    #  'DEFAULT_RENDERER_CLASSES': (
    # 'rest_framework.renderers.JSONRenderer',
    # 'rest_framework.renderers.BrowsableAPIRenderer',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}


# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'

SIMPLEUI_STATIC_OFFLINE = True

SIMPLEUI_HOME_TITLE = '约健后台管理系统'

SIMPLEUI_HOME_INFO = False

# 首页显示最近动作
SIMPLEUI_HOME_ACTION = True

SIMPLEUI_CONFIG = {
    # 在自定义菜单的基础上保留系统模块
    'dynamic': True,
    'system_keep': False,
    'menus': [
        {
            'app': 'club',
            'name': '俱乐部管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/club/club'
        },
        {
            'app': 'club',
            'name': '关注管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/club/attention'
        },
        {
            'app': 'coach',
            'name': '教练管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/club/coach'
        },
        {
            'app': 'activity',
            'name': '活动管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/activity/activity'
        },
        {
            'app': 'train',
            'name': '培训管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/club/train'
        },
        {
            'app': 'activity',
            'name': '报名管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/activity/apply'
        },

        {
            'app': 'auth',
            'name': '比赛管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/contest/contest'
        },
        {
            'app': 'account',
            'name': '用户管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/account/account'
        },
        {
            'app': 'video',
            'name': '视频管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/club/video'
        },
        {
            'app': 'course',
            'name': '课程管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/club/course'
        },
        {
            'app': 'blueprint',
            'name': '晒图管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/blueprint/blueprint'
        },
        {
            'app': 'blueprint',
            'name': '评论管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/blueprint/comment'
        },
        {
            'app': 'blueprint',
            'name': '图片管理',
            'icon': 'fas fa-user-shield',
            'url': '/admin/blueprint/picture'
        },
    ]
}




JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),    #也可以设置seconds=20
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=30),    #也可以设置seconds=20
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}