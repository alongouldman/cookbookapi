from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from cookbookapi.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'Recipes', views.RecipeViewSet)
router.register(r'Ingredients', views.IngredientViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add-recipe', views.add_recipe)
]


