# Generated by Django 3.1.7 on 2021-02-26 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20210226_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='schedules.company'),
            preserve_default=False,
        ),
    ]
