# Generated by Django 2.2 on 2019-07-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False, verbose_name='活动id')),
                ('activity_title', models.CharField(max_length=256, verbose_name='活动标题')),
                ('activity_desc', models.TextField(max_length=1024, verbose_name='活动简介')),
                ('activity_price', models.IntegerField(verbose_name='活动价格')),
                ('activity_pic', models.CharField(max_length=256, verbose_name='活动宣传图')),
                ('activity_address', models.CharField(max_length=256, verbose_name='活动地点')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动管理',
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('apply_id', models.AutoField(primary_key=True, serialize=False, verbose_name='活动id')),
                ('user_id', models.IntegerField(blank=True, editable=False, null=True, verbose_name='用户id')),
                ('activity_id', models.IntegerField(blank=True, editable=False, null=True, verbose_name='活动id')),
                ('train_id', models.IntegerField(blank=True, editable=False, null=True, verbose_name='培训id')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='报名日期')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'verbose_name': '活动报名',
                'verbose_name_plural': '活动报名管理',
                'db_table': 'apply',
            },
        ),
    ]
