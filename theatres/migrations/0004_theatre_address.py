# Generated by Django 3.1.5 on 2021-01-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatres', '0003_auto_20210112_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='theatre',
            name='address',
            field=models.CharField(default='Timisoara, Romania', max_length=255),
        ),
    ]
