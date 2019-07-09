from django.db import models
from yuejian3.choice import ActivityOrTrainChoice
from club.models import Club

# Create your models here.
class Activity(models.Model):
    activity_id = models.AutoField(verbose_name='活动id',primary_key=True)
    activity_title = models.CharField(max_length=256, verbose_name='活动标题', blank=False, null=False)
    activity_desc = models.TextField(max_length=1024,verbose_name='活动简介',blank=False,null=False)
    activity_price = models.IntegerField(verbose_name='活动价格',blank=False, null=False)
    activity_pic = models.CharField(max_length=256, verbose_name='活动宣传图')
    activity_address = models.CharField(max_length=256, verbose_name='活动地点', blank=False, null=False)
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = "活动管理"
        db_table="activity"

    def __str__(self):
        return self.activityName

class Apply(models.Model):
    apply_id = models.AutoField(verbose_name='活动id',primary_key=True)
    user_id = models.IntegerField(verbose_name='用户id', blank=True, null=True, editable=False)
    activity_id = models.IntegerField(verbose_name='活动id', blank=True, null=True, editable=False)
    train_id = models.IntegerField(verbose_name='培训id', blank=True, null=True,editable = False)
    create_date = models.DateTimeField(verbose_name='报名日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "活动报名"
        verbose_name_plural = "活动报名管理"
        db_table="apply"