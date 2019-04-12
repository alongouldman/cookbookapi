from .models import Ingredient, Recipe
import json

def add_recipe(payload):
	recipe = Recipe(title=payload['title'], instructions=payload['instructions'], image=payload['image'],
					ingredients=json.dumps(payload['ingredients']), overall_time=payload['overall_time'], tags=json.dumps(payload['tags']) if payload.get('tags', False) else None)
	recipe.save()
