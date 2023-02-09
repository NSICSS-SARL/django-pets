# Generated by Django 4.1.6 on 2023-02-09 07:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fructs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="tester_images"),
                ),
                ("name", models.CharField(max_length=50, blank=True, null=True)),
                ("work", models.CharField(max_length=20, blank=True, null=True)),
                ("declaration", models.TextField()),
            ],
        ),
        
        migrations.AddField(
            model_name="testimonial",
            name="note",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="work",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
