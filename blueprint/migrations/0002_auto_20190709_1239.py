# Generated by Django 2.2 on 2019-07-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blueprint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]