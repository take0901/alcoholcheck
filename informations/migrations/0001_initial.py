# Generated by Django 4.1.1 on 2022-12-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Information",
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
                ("year", models.CharField(max_length=10)),
                (
                    "month",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10", "10"),
                            ("11", "11"),
                            ("12", "12"),
                        ],
                        max_length=10,
                    ),
                ),
                ("motouke", models.CharField(max_length=20)),
                ("kouzi", models.CharField(default="", max_length=20)),
                ("place", models.CharField(max_length=20)),
                ("color_number", models.CharField(max_length=30)),
                ("other", models.CharField(max_length=70)),
            ],
        ),
    ]
