# Generated by Django 3.1.5 on 2021-01-12 13:43

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theatres', '0003_auto_20210112_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('shortBio', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='artistImage')),
                ('associatedTheatres', models.ManyToManyField(to='theatres.Theatre')),
            ],
        ),
    ]
