# Generated by Django 4.1 on 2022-09-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fructs', '0005_breadcumb_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
    ]
