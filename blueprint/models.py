from django.db import models

from club.models import Club
# Create your models here.

class Blueprint(models.Model):
    blueprint_id = models.CharField(max_length=11, verbose_name='晒图id', blank=True, null=True, editable=False, db_index=True)
    blueprint_content = models.CharField(max_length=40, verbose_name='内容', blank=False, null=False)
    blueprint_picture = models.CharField(max_length=40, verbose_name='图片', blank=False, null=False)
    create_time = models.DateTimeField(verbose_name='发布时间',blank=False, null=False)
    club_id = models.ForeignKey(Club,on_delete=models.CASCADE,verbose_name='俱乐部id', null=False)


    class Meta:
        verbose_name = "晒图"
        verbose_name_plural = "晒图管理"
        db_table = "blueprint"

    def __str__(self):
        return self.blueprint_id

class Comment(models.Model):
    comment_id = models.CharField(max_length=11, verbose_name='评论ID', blank=True, null=True, editable=False, db_index=True)
    comment_user_id = models.CharField(max_length=11, verbose_name='用户id', blank=False, null=False)
    comment_content = models.TextField(max_length=1024,verbose_name='评论内容')
    comment_time = models.DateTimeField(verbose_name='评论时间',blank=False, null=False)
    # photo_id = models.CharField(max_length=11, verbose_name='图片ID', blank=True, null=True)
    blueprint_id = models.ForeignKey(Club,on_delete=models.CASCADE,verbose_name='晒图id', null=False)
    # from_user_id = models.CharField(max_length=11, verbose_name='评论用户id', blank=False, null=False)
    # to_user_id = models.CharField(max_length=11, verbose_name='被评论用户id', blank=False, null=False)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论管理"
        db_table = "comment"

    def __str__(self):
        return self.comment_id

class Picture(models.Model):
    picture_id = models.CharField(max_length=11, verbose_name='图片id', blank=True, null=True, editable=False, db_index=True)
    picture_address = models.CharField(max_length=11, verbose_name='图片地址', blank=False, null=False)
    create_time = models.DateTimeField(verbose_name='创建时间',blank=False, null=False)

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = "图片管理"
        db_table = "picture"

    def __str__(self):
        return self.picture_id