# Generated by Django 4.1.1 on 2022-12-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("informations", "0002_alter_information_month_alter_information_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information", name="month", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="information", name="year", field=models.IntegerField(),
        ),
    ]
