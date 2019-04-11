from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recipe
from .models import Ingredient

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url', 'title', 'image', 'Ingredients', 'description', 'date_created')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'url', 'name')
