from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from cookbookapi.api import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'recipes', views.RecipeViewSet)
# router.register(r'ingredients', views.IngredientViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path(r'admin/', admin.site.urls),
    path(r'recipes/', views.RecipeList.as_view()),
    re_path(r'ingredients/', views.IngredientList.as_view()),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


