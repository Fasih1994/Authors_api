# Generated by Django 4.1.7 on 2024-02-02 13:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ratings", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rating",
            old_name="ratings",
            new_name="rating",
        ),
    ]
