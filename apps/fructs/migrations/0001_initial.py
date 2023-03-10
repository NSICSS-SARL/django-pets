# Generated by Django 4.1.6 on 2023-02-09 07:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Breadcumb",
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
                ("slug", models.SlugField()),
                ("subtitle", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Categorie",
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
                ("label", models.CharField(default="", max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mail",
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
                ("email", models.CharField(max_length=50)),
                ("subject", models.CharField(max_length=100)),
                ("message", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="SubscribedUsers",
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
                ("email", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subscriber",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("conf_num", models.CharField(max_length=15)),
                ("confirmed", models.BooleanField(default=False)),
            ],
        ),
       
        migrations.CreateModel(
            name="Unitie",
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
                ("unite", models.CharField(default="", max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=100)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="product_images"
                    ),
                ),
                ("sante", models.TextField(default="")),
                (
                    "label",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fructs.categorie",
                    ),
                ),
                (
                    "unite",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="fructs.unitie",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]
