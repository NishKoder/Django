# Generated by Django 4.2.4 on 2023-08-06 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("vtitle", models.CharField(max_length=20)),
                ("vdesc", models.TextField()),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
