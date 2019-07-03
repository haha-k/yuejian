from django.db import models
from club.models import Club

# Create your models here.

class Video(models.Model):
    video_id = models.CharField(max_length=11, verbose_name='视频ID', blank=True, null=True, editable=False, db_index=True) #     club_administrator_id = models.CharField(max_length=11, verbose_name='俱乐部管理员ID', blank=False, null=False)
    video_name = models.TextField(max_length=20,verbose_name='视频标题')
    video_type = models.CharField(max_length=30,verbose_name='视频类型', blank=False, null=False)
    video_pic = models.CharField(max_length=30,verbose_name='视频封面图', blank=False, null=False)
    club_id = models.ForeignKey(Club,on_delete=models.CASCADE,verbose_name='俱乐部id', null=False)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = "视频管理"
        db_table = "video"

    def __str__(self):
        return self.video_name