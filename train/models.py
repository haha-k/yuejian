from django.db import models
from club.models import Club

# Create your models here.

class Train(models.Model):
    train_id = models.CharField(max_length=20, verbose_name='培训标识', blank=True, null=True, editable=False, db_index=True)
    train_title = models.CharField(max_length=10, verbose_name='培训标题', blank=False, null=False)
    train_address = models.CharField(max_length=40, verbose_name='培训地点', blank=False, null=False)
    train_date = models.DateTimeField(verbose_name='培训日期',blank=False, null=False)
    train_price = models.CharField(max_length=5, verbose_name='培训价格',blank=False, null=False)
    train_show = models.TextField(max_length=100,verbose_name='培训简介')
    club_id = models.ForeignKey(Club,on_delete=models.CASCADE,verbose_name='俱乐部id', null=False)


    class Meta:
        verbose_name = "培训"
        verbose_name_plural = "培训管理"
        db_table = "train"

    def __str__(self):
        return self.train_title