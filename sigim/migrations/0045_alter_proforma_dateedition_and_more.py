# Generated by Django 4.2.7 on 2024-05-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0044_alter_proforma_dateedition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proforma',
            name='dateedition',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='proforma',
            name='delaispaiement',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
