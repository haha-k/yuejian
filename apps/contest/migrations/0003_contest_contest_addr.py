# Generated by Django 2.2 on 2019-08-31 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_auto_20190831_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='contest_addr',
            field=models.CharField(max_length=256, null=True, verbose_name='比赛地点'),
        ),
    ]