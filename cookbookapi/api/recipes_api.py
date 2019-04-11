from .models import Ingredient, Recipe
import json

def add_recipe(payload):
	recipe = Recipe(ingredients=json.loads(payload['ingredients']))
	recipes = Recipe.objects.all().values('ingredients')
	Ingredient.objects.filter(name__in=['egg', 'bacon', 'tomato']).distinct('name')



	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	# title = models.CharField(max_length=32)
	# image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	# ingredients = models.CharField()
	# description = models.CharField(max_length=200, default='')
	# date_created = models.DateTimeField(default=datetime.now)