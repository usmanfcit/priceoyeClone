# Generated by Django 5.1 on 2024-09-04 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="created_at",
        ),
    ]
