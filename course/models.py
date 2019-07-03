from django.db import models
from .models import *
from club.models import Club

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=11, verbose_name='教练id', blank=True,null=True, editable=False, db_index=True)
    course_title = models.CharField(max_length=20, verbose_name='标题', blank=False, null=False,editable=True)
    course_intro = models.CharField(max_length=20,verbose_name='简介', blank=False, null=False)
    # club_id = models.CharField(max_length=20,verbose_name='俱乐部id', blank=False, null=False)
    club_id = models.ForeignKey(Club,on_delete=models.CASCADE,verbose_name="俱乐部id")
    course_cover = models.CharField(max_length=30,verbose_name='封面', blank=False, null=False)
    course_site = models.CharField(max_length=30,verbose_name='地点', editable=False)
    course_type = models.CharField(max_length=30,verbose_name='类型',editable=True)

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程管理"
        db_table = "course"