# Generated by Django 3.2.5 on 2021-07-28 22:21

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='My Bio', max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]