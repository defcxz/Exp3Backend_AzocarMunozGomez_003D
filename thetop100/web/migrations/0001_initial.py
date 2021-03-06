# Generated by Django 3.2.3 on 2021-06-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomApellido', models.CharField(max_length=50, verbose_name='Nombre y Apellido')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('telefono', models.IntegerField(max_length=12, verbose_name='Telefono')),
                ('asunto', models.CharField(max_length=50, verbose_name='Asunto')),
                ('mensaje', models.CharField(max_length=500, verbose_name='Mensaje')),
            ],
        ),
    ]
