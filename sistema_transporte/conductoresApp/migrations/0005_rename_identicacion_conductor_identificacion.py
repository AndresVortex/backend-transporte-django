# Generated by Django 4.2 on 2023-05-04 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conductoresApp', '0004_alter_conductor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conductor',
            old_name='identicacion',
            new_name='identificacion',
        ),
    ]
