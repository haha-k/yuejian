from django.db import models
from account.models import Account

# Create your models here.

class Club(models.Model):
    club_id = models.AutoField(verbose_name='俱乐部id',primary_key=True)
    club_name = models.CharField(max_length=20, verbose_name='标题', blank=False, null=False)
    club_desc = models.TextField(max_length=4096,verbose_name='简介')
    hits = models.IntegerField(verbose_name='点击量', default=0, editable=False)
    fans = models.IntegerField(verbose_name='关注量', default=0, editable=False)
    club_phone = models.CharField(max_length=11, verbose_name='联系电话', blank=False, null=False,editable = False)
    club_email = models.EmailField(max_length=30, verbose_name='联系邮箱', blank=False, null=False,editable=False)
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)
    club_head = models.ForeignKey(Picture, on_delete=models.SET_NULL, verbose_name='俱乐部头像',blank = True,null=True)
    # clubAdministrator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='发布者', null=True, editable=False)

    class Meta:
        verbose_name = "俱乐部"
        verbose_name_plural = "俱乐部管理"
        db_table = "club"

    def __str__(self):
        return self.clubName


class Attention(models.Model):
    attention_id = models.AutoField(verbose_name='关注id',primary_key=True)
    club_id = models.IntgerField(verbose_name='俱乐部id')
    user_id = models.IntgerField(verbose_name='用户id')
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "关注"
        verbose_name_plural = "关注管理"
        db_table = "attention"

# class Course(models.Model):
#     clubId = models.CharField(max_length=8, verbose_name='俱乐部ID', blank=True, null=True, editable=False, db_index=True)
#     clubName = models.CharField(max_length=256, verbose_name='标题', blank=False, null=False)
#     clubDesc = models.TextField(max_length=1024,verbose_name='简介')
#     # clubAdministrator = models.CharField(verbose_name='俱乐部管理员', null=True, editable=False)
#     # clubAdministrator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='发布者', null=True, editable=False)
#     hits = models.IntegerField(verbose_name='点击量', default=0, editable=False)
#     fans = models.IntegerField(verbose_name='关注量', default=0, editable=False)
#     image = models.ImageField(upload_to='static/images/', verbose_name='头像', blank=True, null=True, db_index=True)
#     createDate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

#     # def comment_count(self):
#     #     return Comment.objects.filter(targetId=self.id, type=0).count()

#     # def title_url(self):
#     #     return format_html('<a href="/article/{}" target="_blank">{}</a>', self.sid, self.title)

#     # title_url.short_description = "标题"
#     # comment_count.short_description = "评论数"

#     class Meta:
#         verbose_name = "俱乐部"
#         verbose_name_plural = "俱乐部管理"

#     def __str__(self):
#         return self.clubName

