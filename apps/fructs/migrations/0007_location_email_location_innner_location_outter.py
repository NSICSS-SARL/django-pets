# Generated by Django 4.1.6 on 2023-02-10 04:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fructs", "0006_location_title_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="email",
            field=models.EmailField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name="location",
            name="innner",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="location",
            name="outter",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
