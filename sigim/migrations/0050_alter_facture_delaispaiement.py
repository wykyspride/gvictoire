# Generated by Django 4.2.7 on 2024-05-22 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0049_remove_facture_contrat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='delaispaiement',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
