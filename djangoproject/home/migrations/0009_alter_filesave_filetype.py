# Generated by Django 4.2.1 on 2023-05-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_filesave_filesize_filesave_filetype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filesave",
            name="filetype",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
