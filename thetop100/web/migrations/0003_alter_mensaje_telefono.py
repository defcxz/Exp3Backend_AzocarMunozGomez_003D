# Generated by Django 3.2.3 on 2021-06-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_mensaje_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='telefono',
            field=models.CharField(max_length=12, verbose_name='Telefono'),
        ),
    ]
