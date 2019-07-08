from django.db import models
from club.models import Club

# Create your models here.

class Video(models.Model):
    video_id = models.AutoField(verbose_name='视频id',primary_key=True)
    video_title = models.TextField(max_length=20,verbose_name='视频标题')
    video_type = models.CharField(max_length=30,verbose_name='视频类型')
    video_pic = models.CharField(max_length=30,verbose_name='视频封面图')
    club_id = models.ForeignKey(Club,on_delete=models.SET_NULL,verbose_name='俱乐部id', null=False)
    create_date = models.DateTimeField(verbose_name='上传日期', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = "视频管理"
        db_table = "video"

    def __str__(self):
        return self.video_name