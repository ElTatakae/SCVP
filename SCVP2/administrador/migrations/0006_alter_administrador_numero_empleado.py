# Generated by Django 4.2 on 2024-02-13 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_rename_numeroempleado_administrador_numero_empleado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='numero_Empleado',
            field=models.CharField(max_length=100),
        ),
    ]
