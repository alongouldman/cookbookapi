from .models import Ingredient


def add_ingredient(ingredient):
	ing = Ingredient(name=ingredient['name'])
	ing.save()
