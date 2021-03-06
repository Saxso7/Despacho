# Generated by Django 4.0.4 on 2022-06-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroSeguimiento', models.CharField(default='DEFAULT VALUE', max_length=30)),
                ('nombreCliente', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('direccionCliente', models.CharField(default='DEFAULT VALUE', max_length=200)),
                ('horaLlegadaCrear', models.DateTimeField(auto_now_add=True)),
                ('horaLlegadaActualizar', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'despacho',
            },
        ),
    ]
