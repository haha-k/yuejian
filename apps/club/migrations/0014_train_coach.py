# Generated by Django 2.2 on 2019-08-31 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0013_auto_20190831_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='coach',
            field=models.ForeignKey(db_column='coach_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='club.Coach', verbose_name='教练id'),
        ),
    ]
