# Generated by Django 4.2.11 on 2024-04-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0009_record_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("student_id", models.IntegerField(max_length=15)),
            ],
        ),
    ]