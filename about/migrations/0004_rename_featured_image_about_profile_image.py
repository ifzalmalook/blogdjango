# Generated by Django 4.2.10 on 2024-03-01 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='featured_image',
            new_name='profile_image',
        ),
    ]
