from django.contrib import admin
from cookbookapi.api.models import Recipe, Ingredient

admin.site.register(Recipe)
admin.site.register(Ingredient)
