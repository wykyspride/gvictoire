# Generated by Django 4.2.7 on 2024-04-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0037_rename_lignedevis_prestattions'),
    ]

    operations = [
        migrations.CreateModel(
            name='prestations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=105)),
                ('montant', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='prestattions',
        ),
    ]
