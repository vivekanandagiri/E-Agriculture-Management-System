# Generated by Django 5.1 on 2024-11-01 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0025_alter_profile_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="uid",
            field=models.CharField(
                default="<function uuid4 at 0x000001BF4F3414E0>", max_length=200
            ),
        ),
    ]
