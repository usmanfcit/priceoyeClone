# Generated by Django 5.1 on 2024-08-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_alter_orderitem_options_orderitem_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="activate_date",
            field=models.DateTimeField(
                blank=True,
                help_text="keep empty for an immediate activation",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="deactivate_date",
            field=models.DateTimeField(
                blank=True, help_text="keep empty for indefinite activation", null=True
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Inactive"), (1, "Active")],
                default=1,
                verbose_name="status",
            ),
        ),
    ]
