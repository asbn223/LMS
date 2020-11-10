# Generated by Django 3.1.3 on 2020-11-10 06:10

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='img',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]