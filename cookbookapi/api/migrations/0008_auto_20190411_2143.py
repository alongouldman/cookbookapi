# Generated by Django 2.2 on 2019-04-11 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_merge_20190411_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Ingredients',
            new_name='ingredients',
        ),
    ]