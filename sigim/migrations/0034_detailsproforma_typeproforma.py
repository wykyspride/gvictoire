# Generated by Django 4.2.7 on 2024-04-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0033_facture_typefacture_proforma_mandat_detailsproforma_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailsproforma',
            name='typeproforma',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
