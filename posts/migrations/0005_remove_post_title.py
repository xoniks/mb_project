# Generated by Django 4.1.3 on 2022-11-03 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
