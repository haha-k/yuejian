from django.db import models
from club.models import *

# Create your models here.

class Coach(models.Model):
    coach_id = models.CharField(max_length=11, verbose_name='教练id', blank=True,null=True, editable=False, db_index=True)
    coach_name = models.CharField(max_length=20, verbose_name='姓名', blank=False, null=False,editable=True)
    coach_phone = models.CharField(max_length=20,verbose_name='电话', blank=False, null=False)
    # club_id = models.CharField(max_length=20,verbose_name='俱乐部id', blank=False, null=False)
    club_id = models.ForeignKey(Club,on_delete=models.CASCADE,verbose_name='俱乐部id', null=False)
    coach_email = models.CharField(max_length=30,verbose_name='邮箱', blank=False, null=False)
    coach_age = models.IntegerField(verbose_name='年龄', editable=True)
    coach_seniority = models.IntegerField(verbose_name='教龄',editable=True)
    coach_ismaster = models.IntegerField(verbose_name='是否大师', default=0)

    def __str__(self):
        return self.coach_name

    class Meta:
        verbose_name = "教练"
        verbose_name_plural = "教练管理"
        db_table = "coach"



#     video_id = models.CharField(max_length=11, verbose_name='视频ID', blank=True, null=True, editable=False, db_index=True)
#     club_administrator_id = models.CharField(max_length=11, verbose_name='俱乐部管理员ID', blank=False, null=False)
#     video_name = models.TextField(max_length=20,verbose_name='视频标题')
#     video_type = models.CharField(verbose_name='视频类型', blank=False, null=False)

#     class Meta:
#         verbose_name = "视频"
#         verbose_name_plural = "视频管理"

#     def __str__(self):
#         return self.contestName

#     system_administrator_id = models.CharField(max_length=11, verbose_name='系统管理员ID', blank=True, null=True, editable=False, db_index=True)
#     system_administrator_userid = models.CharField(max_length=11, verbose_name='账号', blank=False, null=False)
#     system_administrator_password = models.CharField(max_length=20, verbose_name='密码', blank=False, null=False)
#     system_administrator_name = models.TextField(max_length=20,verbose_name='昵称')
#     system_administrator_phone = models.IntegerField(max_length=20,verbose_name='联系电话', default=0, editable=False)
#     system_administrator_email = models.CharField(max_length=30, verbose_name='邮箱', blank=False, null=False)
#     system_administrator_portrait = models.CharField( verbose_name='头像', blank=False, null=False)

#     class Meta:
#         verbose_name = "系统管理员"
#         verbose_name_plural = "系统管理员管理"

#     def __str__(self):
#         return self.contestName



# class User(models.Model):
#     userId = models.CharField(max_length=20, verbose_name='用户id', blank=True, null=True, editable=False, db_index=True)
#     userName = models.CharField(max_length=10, verbose_name='用户名', blank=True, null=True)
#     userNickname = models.CharField(max_length=20, verbose_name='用户昵称', blank=True, null=True)
#     userPassword = models.CharField(max_length=10, verbose_name='用户密码', blank=True, null=True)
#     userEmail = models.CharField(max_length=20, verbose_name='用户邮箱', blank=True, null=True)
#     userPhone = models.CharField(max_length=11, verbose_name='用户联系电话', blank=True, null=True)
#     userPrice = models.CharField(max_length=15, verbose_name='用户头像', blank=True, null=True)

#     class Meta:
#         verbose_name = "用户"
#         verbose_name_plural = "用户管理"

#     def __str__(self):
#         return self.userName


# class Clubadmin(models.Model):
#     clubadminId = models.CharField(max_length=20, verbose_name='俱乐部管理员id', blank=True, null=True, editable=False, db_index=True)
#     clubadminName = models.CharField(max_length=10, verbose_name='俱乐部管理员用户名', blank=True, null=True)
#     clubadminOname = models.CharField(max_length=20, verbose_name='俱乐部管理员名称', blank=True, null=True)
#     clubadminPassword = models.CharField(max_length=10, verbose_name='俱乐部管理员密码', blank=True, null=True)
#     clubadminEmail = models.CharField(max_length=20, verbose_name='俱乐部管理员邮箱', blank=True, null=True)
#     clubadminPhone = models.CharField(max_length=11, verbose_name='俱乐部管理员电话', blank=True, null=True)
#     clubadminPrice = models.CharField(max_length=15, verbose_name='俱乐部管理员头像', blank=True, null=True)

#     class Meta:
#         verbose_name = "俱乐部管理员"
#         verbose_name_plural = "俱乐部管理员管理"

#     def __str__(self):
#         return self.clubadminName