# Generated by Django 3.2 on 2021-06-25 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_image_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='subjects',
            new_name='subject',
        ),
    ]
