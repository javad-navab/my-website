# Generated by Django 3.2.4 on 2023-09-09 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approach',
            new_name='approved',
        ),
    ]