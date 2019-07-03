from django.contrib import admin
#新加入的包
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


#此处更改，相当于创了另一个页面
class MyAdminSite(AdminSite):
    #网站标签页标题
    site_title = ugettext_lazy('约健后台管理系统')
    #网站标题
    site_header = ugettext_lazy('约健后台管理系统')

admin.site = MyAdminSite()
