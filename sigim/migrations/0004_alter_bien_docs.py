# Generated by Django 4.2.7 on 2024-03-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0003_alter_bien_typebien_delete_typebien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bien',
            name='docs',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
