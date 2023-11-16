# Generated by Django 4.2.7 on 2023-11-16 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Atividade",
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
                ("tempo_atividade", models.CharField(max_length=50)),
                ("usuario_id", models.EmailField(max_length=254, unique=True)),
                ("atividade_id", models.IntegerField()),
                ("created_at", models.CharField(max_length=50)),
            ],
        ),
    ]