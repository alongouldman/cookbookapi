from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime


def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)


class Ingredient(models.Model):
	name = models.CharField(max_length=200, null=True)
	type = models.CharField(max_length=200, null=True)
	protein = models.FloatField(max_length=200, null=True)
	carbohydrate = models.FloatField(max_length=200, null=True)
	fat = models.FloatField(max_length=200, null=True)
	calories = models.FloatField(max_length=200, null=True)
	sugar = models.FloatField(max_length=200, null=True)
	vitamin_C = models.FloatField(max_length=200, null=True)
	vitamin_B1 = models.FloatField(max_length=200, null=True)
	vitamin_B2 = models.FloatField(max_length=200, null=True)
	vitamin_B3 = models.FloatField(max_length=200, null=True)
	vitamin_B6 = models.FloatField(max_length=200, null=True)
	sodium = models.FloatField(max_length=200, null=True)
	phosphorus = models.FloatField(max_length=200, null=True)
	magnesium = models.FloatField(max_length=200, null=True)
	iron = models.FloatField(max_length=200, null=True)
	calcium = models.FloatField(max_length=200, null=True)
	potassium = models.FloatField(max_length=200, null=True)
	nutritional_fiber = models.FloatField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Recipe(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=32)
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	ingredients = models.CharField(max_length=5000, null=True)
	description = models.CharField(max_length=200, null=True, default='')
	date_created = models.DateTimeField(default=datetime.now)
