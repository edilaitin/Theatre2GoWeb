# Generated by Django 3.1.5 on 2021-01-12 13:43

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theatres', '0003_auto_20210112_1429'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaultPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('shortBio', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='playImage')),
                ('carouselImage1', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='carouselImage1')),
                ('carouselImage2', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='carouselImage2')),
                ('carouselImage3', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='carouselImage3')),
                ('active', models.BooleanField(default=True)),
                ('actors', models.ManyToManyField(related_name='actors', to='artists.Artist')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='artists.artist')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theatres.theatre')),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('vaultPlay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plays.vaultplay')),
            ],
        ),
    ]
