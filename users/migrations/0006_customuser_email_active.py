# Generated by Django 5.1.2 on 2024-12-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_profilemodel_available_words"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="email_active",
            field=models.BooleanField(default=False),
        ),
    ]