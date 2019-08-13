from django.db import models

# Create your models here.
class Contest(models.Model):
    contest_id = models.AutoField(verbose_name='比赛id',primary_key = True)
    contest_title = models.CharField(max_length=40, verbose_name='比赛标题', blank=False, null=False)
    contest_pic = models.CharField(max_length=256, verbose_name='比赛宣传图')
    contest_desc = models.TextField(max_length=4096,verbose_name='比赛简介')
    contest_date = models.DateTimeField(verbose_name='比赛日期',blank=False, null=False)
    create_date = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "比赛"
        verbose_name_plural = "比赛管理"
        db_table = "contest"

    def __str__(self):
        return self.contest_title