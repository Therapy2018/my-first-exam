# Generated by Django 2.2.dev20180822160729 on 2018-08-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='name',
            new_name='task',
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
