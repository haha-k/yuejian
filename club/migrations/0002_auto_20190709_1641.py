# Generated by Django 2.2 on 2019-07-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_administrator',
            field=models.IntegerField(verbose_name='俱乐部管理员'),
        ),
    ]
