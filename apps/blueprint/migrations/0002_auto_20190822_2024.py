# Generated by Django 2.2 on 2019-08-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blueprint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='url',
            field=models.ImageField(upload_to='./static/images/%Y/%m/%d', verbose_name='图片地址'),
        ),
    ]