# Generated by Django 2.1 on 2020-05-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_unloading',
            name='plan_id',
            field=models.AutoField(max_length=255, primary_key=True, serialize=False, verbose_name='卸箱计划编号'),
        ),
    ]
