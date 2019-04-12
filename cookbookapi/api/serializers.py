from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recipe
from .models import Ingredient
from drf_extra_fields.fields import Base64ImageField



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'url', 'title', 'image', 'ingredients', 'description', 'date_created')


class RecipeSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    image = serializers.CharField(required=False)
    ingredients = serializers.ListField(required=True)
    tags = serializers.ListField(required=True)
    instructions = serializers.CharField(required=True)
    overall_time = serializers.IntegerField(required=True)
    rate = serializers.FloatField(required=False)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

