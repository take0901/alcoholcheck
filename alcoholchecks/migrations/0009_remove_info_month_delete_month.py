# Generated by Django 4.1.1 on 2022-12-04 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "alcoholchecks",
            "0008_info_owner_alter_info_alcohol_alter_info_carnumber_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="info", name="month",),
        migrations.DeleteModel(name="Month",),
    ]
