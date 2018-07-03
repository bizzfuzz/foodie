from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .models import Ingredient
from .models import Direction
from .models import Nutrition
from django.utils import timezone

# Create your views here.
def recipeList(request):
    recipes = Recipe.objects.filter(publishDate__lte =  timezone.now()).order_by('publishDate')
    return render(request, 'foodie/recipeList.html', {'recipes': recipes})

def recipeInfo(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = Ingredient.objects.filter(recipe__pk = recipe.pk)
    directions = Direction.objects.filter(recipe__pk = recipe.pk).order_by('number')
    return render(request, 'foodie/recipeInfo.html', {'recipe': recipe, 'ingredients': ingredients, 'directions': directions})
