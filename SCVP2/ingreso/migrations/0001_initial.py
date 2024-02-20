

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('auth', '0012_alter_user_first_name_max_length'),


    ]

    operations = [
        migrations.CreateModel(

            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('numero_empleado', models.IntegerField(unique=True)),
                ('is_operador', models.BooleanField(default=False)),
                ('is_lider', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', related_query_name='customuser', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', related_query_name='customuser', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },

        ),
    ]
