# Generated by Django 5.0.3 on 2024-04-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Email",
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
                ("name", models.CharField(max_length=100, verbose_name="nombre")),
                (
                    "email",
                    models.EmailField(
                        max_length=150, unique=True, verbose_name="correo electronico"
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="hora")),
            ],
        ),
    ]
