from django.db import models
from yuejian3.choice import ActivityOrTrainChoice
from club.models import Club

# Create your models here.
class Activity(models.Model):
    activityId = models.CharField(max_length=8, verbose_name='活动ID', blank=True, null=True, editable=False, db_index=True)
    activityName = models.CharField(max_length=256, verbose_name='活动名称', blank=False, null=False)
    activityDesc = models.TextField(max_length=1024,verbose_name='活动简介')
    activityPrice = models.CharField(max_length=5, verbose_name='活动价格',blank=False, null=False)
    # clubAdministrator = models.CharField(verbose_name='俱乐部管理员', null=True, editable=False)
    # clubAdministrator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='发布者', null=True, editable=False)
    hits = models.IntegerField(verbose_name='点击量', default=0, editable=False)
    fans = models.IntegerField(verbose_name='报名人数', default=0, editable=False)
    image = models.ImageField(upload_to='static/images/', verbose_name='头像',blank=True, null=True, db_index=True)
    createDate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    # def comment_count(self):
    #     return Comment.objects.filter(targetId=self.id, type=0).count()

    # def title_url(self):
    #     return format_html('<a href="/article/{}" target="_blank">{}</a>', self.sid, self.title)

    # title_url.short_description = "标题"
    # comment_count.short_description = "评论数"

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = "活动管理"
        db_table="activity"

    def __str__(self):
        return self.activityName

class Apply(models.Model):
    userId = models.CharField(max_length=8, verbose_name='用户ID', blank=True, null=True, editable=False, db_index=True)
    userName = models.CharField(max_length=256, verbose_name='用户名称', blank=False, null=False)
    aotId = models.CharField(max_length=8, verbose_name='ID', blank=True, null=True, editable=False)
    activityOrTrain = models.IntegerField(choices=ActivityOrTrainChoice,verbose_name="培训/活动",blank=True, null=True, editable=False)
    aotName = models.CharField(max_length=256, verbose_name='名称', blank=False, null=False)
    createDate = models.DateTimeField(verbose_name='报名日期', auto_now_add=True)

    class Meta:
        verbose_name = "活动报名"
        verbose_name_plural = "活动报名管理"
        db_table="apply"

