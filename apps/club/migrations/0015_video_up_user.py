# Generated by Django 2.2 on 2019-08-31 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0014_train_coach'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='up_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='上传人'),
        ),
    ]
