# Generated by Django 2.1 on 2020-05-04 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_auto_20200504_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_unloading',
            name='job_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='任务id'),
        ),
    ]
