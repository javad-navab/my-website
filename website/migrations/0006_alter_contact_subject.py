# Generated by Django 3.2.4 on 2023-08-31 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]