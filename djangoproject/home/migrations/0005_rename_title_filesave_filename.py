# Generated by Django 4.2.1 on 2023-05-20 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_filesave_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="filesave",
            old_name="title",
            new_name="filename",
        ),
    ]