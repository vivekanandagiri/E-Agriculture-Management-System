# Generated by Django 5.1 on 2024-11-01 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0021_alter_profile_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="uid",
            field=models.CharField(
                default="<function uuid4 at 0x00000250851C14E0>", max_length=200
            ),
        ),
    ]
