# Generated by Django 4.2.7 on 2024-04-19 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0026_remove_proprietaire_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='employeurloca',
        ),
        migrations.RemoveField(
            model_name='client',
            name='photoloca',
        ),
    ]
