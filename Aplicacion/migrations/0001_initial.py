# Generated by Django 4.0.5 on 2023-02-14 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.IntegerField(verbose_name='30')),
                ('Descripcion', models.CharField(max_length=30)),
                ('Fecha', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apelllido', models.CharField(max_length=50)),
                ('F_Nacimiento', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=10)),
                ('Clave', models.CharField(max_length=30)),
                ('id_Rol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion.rol')),
            ],
        ),
    ]
