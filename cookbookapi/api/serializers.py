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
        fields = ('id', 'url', 'title', 'image', 'ingredients', 'description', 'date_created')


class IngredientSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = serializers.ListField(serializers.DictField(['name', 'amount', 'unit']))
        fields = ('id', 'url', 'name')
