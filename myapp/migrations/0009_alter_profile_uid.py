# Generated by Django 5.1 on 2024-10-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_alter_profile_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="uid",
            field=models.CharField(
                default="<function uuid4 at 0x0000021F85CC14E0>", max_length=200
            ),
        ),
    ]
