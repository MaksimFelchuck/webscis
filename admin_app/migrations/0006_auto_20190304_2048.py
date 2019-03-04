# Generated by Django 2.0.5 on 2019-03-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_auto_20190304_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectright',
            old_name='right',
            new_name='can_exec',
        ),
        migrations.AddField(
            model_name='projectright',
            name='can_read',
            field=models.CharField(choices=[('Choice1', 'True'), ('Choice2', 'False')], default='False', max_length=20),
        ),
        migrations.AddField(
            model_name='projectright',
            name='can_write',
            field=models.CharField(choices=[('Choice1', 'True'), ('Choice2', 'False')], default='False', max_length=20),
        ),
    ]
