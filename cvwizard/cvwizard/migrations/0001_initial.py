# Generated by Django 4.2.7 on 2023-11-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_name", models.CharField(max_length=200)),
                ("first_name", models.CharField(max_length=200)),
                ("birthdate", models.DateField(verbose_name="date of birth")),
            ],
        ),
    ]
