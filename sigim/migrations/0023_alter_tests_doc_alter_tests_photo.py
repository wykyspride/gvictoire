# Generated by Django 4.2.7 on 2024-04-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigim', '0022_rename_test_tests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='doc',
            field=models.FileField(blank=True, default='', upload_to='filetest/'),
        ),
        migrations.AlterField(
            model_name='tests',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='imagetest/'),
        ),
    ]
