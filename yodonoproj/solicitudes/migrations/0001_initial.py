# Generated by Django 2.2 on 2020-03-19 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('edad', models.CharField(max_length=2)),
                ('hospital', models.CharField(max_length=40)),
                ('grupoSanguineo', models.CharField(max_length=11)),
                ('fechaLimite', models.DateField()),
                ('motivo', models.CharField(max_length=90)),
                ('cantidadDonantes', models.IntegerField()),
                ('departamento', models.CharField(max_length=30)),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]