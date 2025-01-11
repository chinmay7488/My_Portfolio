# Generated by Django 5.0.8 on 2024-11-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomePage_model",
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
                ("Job_titles", models.JSONField()),
                ("Sub_heading_into", models.CharField(max_length=500)),
                ("profile_pic", models.FileField(upload_to="ProfilePhoto/")),
                ("facebook_url", models.CharField(max_length=500, null=True)),
                ("instagram_url", models.CharField(max_length=500, null=True)),
                ("twitter_url", models.CharField(max_length=500, null=True)),
                ("github_url", models.CharField(max_length=500, null=True)),
                ("linkedin_url", models.CharField(max_length=500, null=True)),
                ("resume_url", models.CharField(max_length=500, null=True)),
            ],
        ),
    ]