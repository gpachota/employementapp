# Generated by Django 3.1.7 on 2021-03-01 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0008_auto_20210226_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='holiday_days_count',
            field=models.IntegerField(default=0),
        ),
    ]
