from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from cookbookapi.api import views, urls

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'recipes', views.RecipeViewSet)
# router.register(r'ingredients', views.IngredientViewSet)

urlpatterns = [
    path('', include('cookbookapi.api.urls')),
    path(r'admin/', admin.site.urls),

]


