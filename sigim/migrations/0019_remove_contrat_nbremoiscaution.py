# Generated by Django 4.2.7 on 2024-04-11 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0018_alter_compbien_options_compbien_depotgarantie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrat',
            name='nbremoiscaution',
        ),
    ]
