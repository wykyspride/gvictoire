# Generated by Django 4.2.7 on 2024-05-07 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0045_alter_proforma_dateedition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsproforma',
            name='description',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sigim.prestations'),
            preserve_default=False,
        ),
    ]
