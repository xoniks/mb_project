# Generated by Django 4.1.3 on 2022-11-03 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_post_notpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='notPost',
            new_name='Post',
        ),
    ]
