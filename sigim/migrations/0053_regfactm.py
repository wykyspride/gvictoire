# Generated by Django 4.2.7 on 2024-05-22 16:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0052_facture_proprietaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='regfactm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datereg', models.DateField(default=datetime.datetime.today)),
                ('montantregle', models.IntegerField(default=0)),
                ('reste', models.IntegerField(default=0)),
                ('commentaire', models.CharField(default='', max_length=500)),
                ('bien', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sigim.bien')),
                ('facture', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sigim.facture')),
                ('modereglement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigim.modereglement')),
                ('proforma', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sigim.proforma')),
                ('proprietaire', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sigim.proprietaire')),
                ('status', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='sigim.status')),
            ],
            options={
                'verbose_name': 'Reglement Mandat',
                'verbose_name_plural': 'Reglement Mandat',
            },
        ),
    ]
