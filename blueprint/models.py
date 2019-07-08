from django.db import models

from club.models import Club
# Create your models here.

class Blueprint(models.Model):
    blueprint_id = models.AutoField(verbose_name='晒图id',primary_key=True)
    blueprint_content = models.TextField(max_length=2048, verbose_name='晒图内容', blank=False, null=False)
    blueprint_picture = models.CharField(max_length=256, verbose_name='晒图图片', blank=False, null=False)
    create_date = models.DateTimeField(verbose_name='发布时间',blank=False, null=False)
    user_id = models.ForeignKey(User,on_delete=models.SET_NULL,verbose_name='用户id')
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)


    class Meta:
        verbose_name = "晒图"
        verbose_name_plural = "晒图管理"
        db_table = "blueprint"

    def __str__(self):
        return self.blueprint_id

class Comment(models.Model):
    comment_id = models.AutoField(verbose_name='评论id',primary_key=True)
    comment_content = models.TextField(max_length=1024,verbose_name='评论内容')
    comment_time = models.DateTimeField(verbose_name='评论时间',blank=False, null=False)
    # photo_id = models.CharField(max_length=11, verbose_name='图片ID', blank=True, null=True)
    blueprint_id = models.IntegerField(verbose_name='晒图id', null=False)
    from_user_id = models.IntegerField(verbose_name='评论用户id', null=False)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论管理"
        db_table = "comment"

    def __str__(self):
        return self.comment_id

class Picture(models.Model):
    picture_id = models.AutoField(verbose_name='图片id',primary_key=True)
    picture_address = models.ImageField(verbose_name="图片地址",upload='./static/image')
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = "图片管理"
        db_table = "picture"

    def __str__(self):
        return self.picture_id