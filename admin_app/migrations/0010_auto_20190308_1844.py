# Generated by Django 2.0.5 on 2019-03-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0009_auto_20190306_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectright',
            name='can_exec',
            field=models.CharField(default='No', max_length=20),
        ),
        migrations.AlterField(
            model_name='projectright',
            name='can_read',
            field=models.CharField(default='No', max_length=20),
        ),
        migrations.AlterField(
            model_name='projectright',
            name='can_write',
            field=models.CharField(default='No', max_length=20),
        ),
    ]
