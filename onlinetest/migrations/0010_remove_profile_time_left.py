# Generated by Django 2.2.10 on 2021-02-05 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0009_auto_20210205_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='time_left',
        ),
    ]
