# Generated by Django 3.1.5 on 2021-01-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_actorrole'),
        ('plays', '0002_auto_20210112_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaultplay',
            name='actors',
            field=models.ManyToManyField(related_name='actors', to='artists.Artist'),
        ),
    ]
