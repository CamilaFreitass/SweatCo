# Generated by Django 4.2.7 on 2023-11-16 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("perfil", "0002_alter_usuario_empresa"),
        ("atividade_usuario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="atividade",
            name="created_at",
            field=models.DateTimeField(max_length=50),
        ),
        migrations.AlterField(
            model_name="atividade",
            name="tempo_atividade",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="atividade",
            name="usuario_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="perfil.usuario"
            ),
        ),
    ]
