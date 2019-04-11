from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from cookbookapi.api import recipes_api
from cookbookapi.api.serializers import UserSerializer
from .serializers import RecipeSerializer
from .models import Recipe
from .serializers import IngredientSerializer
from .models import Ingredient


@api_view(['POST'])
def add_recipe(request):
	try:
		recipes_api.add_recipe(payload=request.data)
		return status.HTTP_200_OK
	except Exception as e:
		return status.HTTP_500_INTERNAL_SERVER_ERROR


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer
