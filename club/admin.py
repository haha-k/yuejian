from django.contrib import *
from .models import *

# Register your models here.
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('club_id', 'club_name', 'club_desc', 'club_phone','club_email','hits', 'fans', 'club_head', 'create_date','update_date')
    list_filter = ('create_date', 'club_name',)
    search_fields = ('club_name',)
    list_display_links = ('club_id', 'club_name')
    # list_editable = ('top', 'category')
    list_per_page = 10


@admin.register(Attention)
class AttentionAdmin(admin.ModelAdmin):
    list_display = ('club_id','user_id','create_date')
    list_filter = ('user_id',)
    search_fields = ('create_date',)
    list_display_links = ('club_id', 'user_id')
    # list_editable = ('top', 'category')
    list_per_page = 10
    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     subject = get_subject(obj.content)
    #     # oss.put_object(obj.image.file.file)
    #     # 不超过200字
    #     if len(subject) > 200:
    #         subject = subject[0:200]

    #     # 短id
    #     if not obj.sid:
    #         obj.sid = short_id.get_short_id()

    #     obj.subject = subject
    #     # 处理标签
    #     tags = obj.tags
    #     # 自动生成
    #     if tags is None or tags is "":
    #         r = analyse.extract_tags(subject, topK=5)
    #         tags = ",".join(r)

    #     obj.tags = tags

    #     # 如果没有封面就生成
    #     if obj.image == '':
    #         total = Cover.objects.count()
    #         c = Cover.objects.all()[random.randint(0, total - 1)]
    #         url = draw.draw(text=obj.title, url=c.image.url, font_size=c.font_size, color=c.color, x=c.x, y=c.y)
    #         obj.image.name = url
    #     super(ArticleAdmin, self).save_model(request, obj, form, change)
    #     cache.delete(cache.CACHE_HOME_KEY)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id','course_title','course_intro', 'club_id', 'course_cover', 'course_site','course_type')
    list_filter = ('course_title', 'club_id',)
    search_fields = ('course_title',)
    list_display_links = ('course_id', 'course_title')
    # list_editable = ('top', 'category')


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_id', 'train_title','train_address', 'train_date', 'train_price', 'train_show','club_id')
    list_filter = ('train_title',)
    search_fields = ('train_title',)
    list_display_links = ('train_id', 'train_title')
    # list_editable = ('top', 'category')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'video_title','video_type', 'video_pic', 'club_id')
    list_filter = ('video_title',)
    search_fields = ('video_title',)
    list_display_links = ('video_id', 'video_title')
    # list_editable = ('top', 'category')


@admin.register(Coach)
class coachAdmin(admin.ModelAdmin):
    list_display = ('coach_id', 'coach_name','coach_phone', 'coach_email', 'coach_age', 'coach_seniority','coach_ismaster')
    list_filter = ('coach_id', 'coach_name',)
    search_fields = ('coach_name',)
    list_display_links = ('coach_id', 'coach_name')
    # list_editable = ('top', 'category')
