from django.db import models
from .models import *
from club.models import Club

# Create your models here.

class Course(models.Model):
    course_id = models.AutoField(verbose_name='课程id',primary_key=True)
    course_title = models.CharField(max_length=20, verbose_name='标题', blank=False, null=False,editable=True)
    course_intro = models.CharField(max_length=20,verbose_name='简介', blank=False, null=False)
    # club_id = models.CharField(max_length=20,verbose_name='俱乐部id', blank=False, null=False)
    club_id = models.ForeignKey(Club,on_delete=models.CASCADE,verbose_name="俱乐部id")
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