# Generated by Django 4.2.7 on 2024-05-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0047_proforma_observation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='contrat',
        ),
        migrations.AddField(
            model_name='facture',
            name='contrat_id',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
