# Generated by Django 4.1.1 on 2022-12-18 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_catnumber"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="catnumber", new_name="carnumber",
        ),
    ]
