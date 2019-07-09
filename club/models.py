from django.db import models
from account.models import Account
from blueprint.models import Picture

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
    club_id = models.IntegerField(verbose_name='俱乐部id')
    user_id = models.IntegerField(verbose_name='用户id')

    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "关注"
        verbose_name_plural = "关注管理"
        db_table = "attention"


