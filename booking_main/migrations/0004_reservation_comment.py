# Generated by Django 3.2.9 on 2021-11-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking_main", "0003_reservation"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="comment",
            field=models.TextField(null=True),
        ),
    ]
