# Generated by Django 5.1.2 on 2024-11-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_content_artices_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content_artices_model",
            name="type",
            field=models.CharField(
                choices=[
                    ("Blog content", "Blog Content"),
                    ("Content write", "Content Write"),
                    ("News content", "News Content"),
                    ("Scientific content", "Scientific Content"),
                    ("Educational content", "Educational Content"),
                    ("Other", "Other"),
                ],
                max_length=50,
            ),
        ),
    ]
