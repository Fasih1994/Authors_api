# Generated by Django 4.1.7 on 2024-01-29 07:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="prifile_photo",
            new_name="profile_photo",
        ),
    ]
