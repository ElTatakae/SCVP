# Generated by Django 4.2 on 2024-02-08 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_remove_customuser_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
