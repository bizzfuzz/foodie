from django.contrib import admin
from .models import Recipe
from .models import Ingredient
from .models import Direction
from .models import Nutrition

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Direction)
admin.site.register(Nutrition)
