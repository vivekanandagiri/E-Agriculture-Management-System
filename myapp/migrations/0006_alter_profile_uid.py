# Generated by Django 5.1 on 2024-10-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_alter_profile_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="uid",
            field=models.CharField(
                default="<function uuid4 at 0x000001E7E51714E0>", max_length=200
            ),
        ),
    ]
