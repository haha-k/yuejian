from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',#设置数据库为mysql
        'NAME':'yuejian3',#数据库名为alldb
        'USER':'root',#数据库用户名
        'PASSWORD':'123',#数据库用户密码
        # 'HOST':'db',
        'OPTIONS':{
            'autocommit':True,
             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


STATIC_URL = '/static/'


# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'

SIMPLEUI_STATIC_OFFLINE = True

SIMPLEUI_HOME_TITLE = '约健后台管理系统'

SIMPLEUI_HOME_INFO = False

#首页显示最近动作
SIMPLEUI_HOME_ACTION = True

SIMPLEUI_CONFIG = {
    # 在自定义菜单的基础上保留系统模块
    'dynamic':True,
    'system_keep': False,
    'menus': [
        # {
    #     'app': 'activity',
    #     'name': '活动管理',
    #     'icon': 'fas fa-user-shield',
    #     'models': [{
    #         'name': '活动基本信息管理',
    #         'icon': 'fa fa-user',
    #         'url': '/admin/activity/activity'
    #     }

    #     ]
    # },
    {
        'app': 'club',
        'name': '俱乐部管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/club/club'
    },
     {
        'app': 'club',
        'name': '关注管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/club/attention'
    },
     {
        'app': 'coach',
        'name': '教练管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/coach/coach'
    },
    #    {
    #     'app': 'master',
    #     'name': '大师管理',
    #     'icon': 'fas fa-user-shield',
    #     'url':'/admin/master/master'
    # },
    {
        'app': 'activity',
        'name': '活动管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/activity/activity'
    },
    {
        'app': 'train',
        'name': '培训管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/train/train'
    },
    {
        'app': 'activity',
        'name': '报名管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/activity/apply'
    },

  {
        'app': 'auth',
        'name': '比赛管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/contest/contest'
    },
    {
        'app': 'account',
        'name': '用户管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/account/account'
    },
    {
        'app': 'video',
        'name': '视频管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/video/video'
    },

    # {
    #     'app': 'train',
    #     'name': '培训管理',
    #     'icon': 'fas fa-user-shield',
    #     'models': [{
    #         'name': '培训基本信息管理',
    #         'icon': 'fa fa-user',
    #         'url': '/admin/train/train'
    #     }]
    # },

    {
        'app': 'course',
        'name': '课程管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/course/course'
    },
    {
        'app': 'blueprint',
        'name': '晒图管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/blueprint/blueprint'
    },
     {
        'app': 'blueprint',
        'name': '评论管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/blueprint/comment'
    },
    {
        'app': 'blueprint',
        'name': '图片管理',
        'icon': 'fas fa-user-shield',
        'url':'/admin/blueprint/picture'
    },

    # {
    #     'app': 'master',
    #     'name': '大师管理',
    #     'icon': 'fas fa-user-shield',
    #     'url':'/admin/master/master'
    # },

    ]
}