# Generated by Django 4.2.7 on 2024-03-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0010_client_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='localite',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
