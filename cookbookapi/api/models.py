from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime


def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)


class Ingredient(models.Model):
	name = models.CharField(max_length=200)


class Recipe(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=32)
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	ingredients = models.CharField(max_length=5000)
	description = models.CharField(max_length=200, default='')
	date_created = models.DateTimeField(default=datetime.now)
