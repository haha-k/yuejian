# Generated by Django 2.2 on 2019-07-09 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('contest_id', models.AutoField(primary_key=True, serialize=False, verbose_name='比赛id')),
                ('contest_title', models.CharField(max_length=40, verbose_name='比赛标题')),
                ('contest_pic', models.CharField(max_length=256, verbose_name='比赛宣传图')),
                ('contest_desc', models.TextField(max_length=4096, verbose_name='比赛简介')),
                ('contest_date', models.DateTimeField(verbose_name='比赛日期')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '比赛',
                'verbose_name_plural': '比赛管理',
                'db_table': 'contest',
            },
        ),
    ]
