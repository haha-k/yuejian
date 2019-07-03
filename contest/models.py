from django.db import models

# Create your models here.
class Contest(models.Model):
    contest_id = models.CharField(max_length=8, verbose_name='比赛id', blank=True, null=True, editable=False, db_index=True)
    contest_name = models.CharField(max_length=256, verbose_name='比赛名称', blank=False, null=False)
    contest_pic = models.CharField(max_length=256, verbose_name='比赛宣传图', blank=False, null=False)
    contest_desc = models.TextField(max_length=1024,verbose_name='比赛简介')
    contest_date = models.DateTimeField(verbose_name='比赛日期',blank=False, null=False)
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    class Meta:
        verbose_name = "比赛"
        verbose_name_plural = "比赛管理"
        db_table = "contest"

    def __str__(self):
        return self.contest_name