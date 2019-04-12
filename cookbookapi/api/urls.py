from django.urls import path, re_path
from cookbookapi.api import views

urlpatterns = [
    # path('recipes/', views.recipe_list),
    # path('', include(router.urls)),
    path(r'recipes', views.RecipeList.as_view()),
    # path(r'recipes/', views.RecipeList.as_view()),
    re_path(r'ingredients', views.IngredientList.as_view()),
    # path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('snippets/<int:pk>/', views.snippet_detail),
]