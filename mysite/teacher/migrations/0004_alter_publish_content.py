# Generated by Django 5.1.3 on 2025-02-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teacher", "0003_alter_publish_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publish",
            name="content",
            field=models.TextField(blank=True, null=True, verbose_name="เนื้อหา"),
        ),
    ]
