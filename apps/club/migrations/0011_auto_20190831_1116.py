# Generated by Django 2.2 on 2019-08-31 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_auto_20190830_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='train_show',
            new_name='train_intro',
        ),
    ]
