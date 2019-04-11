from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from cookbookapi.api.serializers import UserSerializer
from .serializers import RecipeSerializer
from .models import Recipe
from .serializers import IngredientSerializer
from .models import Ingredient


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
