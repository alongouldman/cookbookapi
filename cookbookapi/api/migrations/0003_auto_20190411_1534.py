# Generated by Django 2.2 on 2019-04-11 12:34

import cookbookapi.api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=cookbookapi.api.models.get_image_path),
        ),
    ]
