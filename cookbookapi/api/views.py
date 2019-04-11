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


class RecipeList(APIView):
    def get(self, request):
        recipes = Recipe.objects.all().values()
        return Response(recipes)

    def post(self, request):
        recipe = RecipeSerializer(data=request.data)
        if recipe.is_valid():
            recipe.save()
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
            serializer.save()
            print(serializer.data)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class IngredientViewSet(viewsets.ModelViewSet):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
