from django.db import models
from account.models import Account
from blueprint.models import Picture

# Create your models here.

class Club(models.Model):
    club_id = models.AutoField(verbose_name='俱乐部id',primary_key=True)
    club_name = models.CharField(max_length=20, verbose_name='标题')
    club_desc = models.TextField(max_length=4096,verbose_name='简介')
    hits = models.IntegerField(verbose_name='点击量', default=0, editable=False)
    fans = models.IntegerField(verbose_name='关注量', default=0, editable=False)
    club_phone = models.CharField(max_length=11, verbose_name='联系电话')
    club_email = models.EmailField(max_length=30, verbose_name='联系邮箱')
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)
    club_head = models.IntegerField(verbose_name='俱乐部头像')
    club_administrator = models.IntegerField(verbose_name='俱乐部管理员')
    # club_head = models.ForeignKey(Picture, on_delete=models.SET_NULL, verbose_name='俱乐部头像',blank = True,null=True)
    # clubAdministrator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='发布者', null=True, editable=False)

    class Meta:
        verbose_name = "俱乐部"
        verbose_name_plural = "俱乐部管理"
        db_table = "club"

    def __str__(self):
        return self.club_name


class Attention(models.Model):
    attention_id = models.AutoField(verbose_name='关注id',primary_key=True)
    club_id = models.IntegerField(verbose_name='俱乐部id')
    user_id = models.IntegerField(verbose_name='用户id')
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "关注"
        verbose_name_plural = "关注管理"
        db_table = "attention"


class Course(models.Model):
    course_id = models.AutoField(verbose_name='课程id',primary_key=True)
    course_title = models.CharField(max_length=20, verbose_name='标题', blank=False, null=False,editable=True)
    course_intro = models.CharField(max_length=20,verbose_name='简介', blank=False, null=False)
    club_id = models.IntegerField(verbose_name="俱乐部id")
    course_cover = models.CharField(max_length=30,verbose_name='封面', blank=False, null=False)
    course_duration = models.IntegerField(verbose_name='时长')
    course_site = models.CharField(max_length=30,verbose_name='地点', editable=False)
    course_type = models.CharField(max_length=30,verbose_name='类型',editable=True)
    course_pubdate = models.DateTimeField(verbose_name='上传日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程管理"
        db_table = "course"


class Train(models.Model):
    train_id = models.AutoField(verbose_name='培训id',primary_key=True)
    train_title = models.CharField(max_length=10, verbose_name='培训标题', blank=False, null=False)
    train_address = models.CharField(max_length=40, verbose_name='培训地点', blank=False, null=False)
    train_date = models.DateTimeField(verbose_name='培训日期',blank=False, null=False)
    train_price = models.CharField(max_length=5, verbose_name='培训价格',blank=False, null=False)
    train_show = models.TextField(max_length=100,verbose_name='培训简介')
    club_id = models.IntegerField(verbose_name='俱乐部id')
    create_date = models.DateTimeField(verbose_name='上传日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "培训"
        verbose_name_plural = "培训管理"
        db_table = "train"

    def __str__(self):
        return self.train_title


class Video(models.Model):
    video_id = models.AutoField(verbose_name='视频id',primary_key=True)
    video_title = models.TextField(max_length=20,verbose_name='视频标题')
    video_type = models.CharField(max_length=30,verbose_name='视频类型')
    video_pic = models.CharField(max_length=30,verbose_name='视频封面图')
    club_id = models.IntegerField(verbose_name='俱乐部id')
    create_date = models.DateTimeField(verbose_name='上传日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = "视频管理"
        db_table = "video"

    def __str__(self):
        return self.video_name

class Coach(models.Model):
    coach_id = models.AutoField(verbose_name='教练id',primary_key=True)
    coach_name = models.CharField(max_length=20, verbose_name='姓名', blank=False, null=False,editable=True)
    coach_phone = models.CharField(max_length=20,verbose_name='电话', blank=False, null=False)
    club_id = models.IntegerField(verbose_name='俱乐部id')
    coach_email = models.CharField(max_length=30,verbose_name='邮箱', blank=False, null=False)
    coach_age = models.IntegerField(verbose_name='年龄', editable=True)
    coach_seniority = models.IntegerField(verbose_name='教龄',editable=True)
    coach_ismaster = models.IntegerField(verbose_name='是否大师', default=0)
    coach_redate = models.DateTimeField(verbose_name='注册日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    def __str__(self):
        return self.coach_name

    class Meta:
        verbose_name = "教练"
        verbose_name_plural = "教练管理"
        db_table = "coach"


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