from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from cookbookapi.api.serializers import UserSerializer
from .serializers import RecipeSerializer
from .models import Recipe
from .serializers import IngredientSerializer
from .models import Ingredient
from rest_framework.views import APIView
from rest_framework.response import Response
from cookbookapi.api import ingredient_api, recipes_api
import json


class RecipeList(APIView):
	def get(self, request):
		recipes = list(Recipe.objects.all().values())
		for recipe in recipes:
			recipe['tags'] = json.loads(recipe['tags']) if recipe['tags'] is not None else None
			recipe['ingredients'] = json.loads(recipe['ingredients']) if recipe['ingredients'] is not None else None
		return Response(recipes)

	def post(self, request):
		recipe = RecipeSerializer(data=request.data)
		if recipe.is_valid():
			recipes_api.add_recipe(request.data)
			return Response(recipe.data, status=status.HTTP_201_CREATED)
		return Response(recipe.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserList(APIView):
#     def get(self, request):
#         users = User.objects.all().values()
#         return Response(users)

#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#
# class RecipeViewSet(viewsets.ModelViewSet):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer


class IngredientList(APIView):
	def get(self, request):
		ingredients = Ingredient.objects.all().values()
		return Response(ingredients)

	def post(self, request):
		serializer = IngredientSerializer(data=request.data, context={'request': request})
		if serializer.is_valid():
			ingredient_api.add_ingredient(serializer.data)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class IngredientViewSet(viewsets.ModelViewSet):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
