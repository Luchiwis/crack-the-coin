# Generated by Django 4.2.1 on 2023-08-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("panel", "0005_rename_token_code_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="jugador",
            name="saw_credits",
            field=models.BooleanField(default=False),
        ),
    ]
