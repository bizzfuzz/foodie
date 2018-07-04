from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .models import Ingredient
from .models import Direction
from .models import Nutrition
from .forms import RecipeForm
from .forms import IngredientForm
from .forms import DirectionForm
from .forms import NutritionForm
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

def newRecipe(request):
    #print("meth: " + request.method)
    if request.method == 'POST':
        #print('\nin\n')
        title = formtitle(request)
        desc = formdesc(request)
        ingredient = forming(request)
        ingamount = formingamount(request)
        direction = formdir(request)
        calories = formnutcal(request)
        fat = formnutfat(request)
        carbs = formnutcarbs(request)
        protein = formnutpro(request)
        cholesterol = formnutchol(request)
        sodium = formnutsod(request)

        print("title: " + title)
        print("desc: " + desc)
        print("ing: " + ingredient)
        print("ingamount: " + ingamount)
        print("dir: " + direction)
        print("calories: " + calories)
        print("fat: " + fat)
        print("carbs: " + carbs)
        print("pro: " + protein)
        print("cholesterol: " + cholesterol)
        print("sodium: " + sodium)

        recipe = getRecipeTitle(request)
        print('recipe: ' + recipe)
        return redirect('newRecipe')
    else:
        base = RecipeForm(prefix = 'base')
        ing = IngredientForm(prefix = 'ing')
        dir = DirectionForm(prefix = 'dir')
        nut = NutritionForm(prefix = 'nut')
        return render(request, 'foodie/recipeEdit.html', {
        'base': base, 'ing': ing, 'dir': dir, 'nut': nut,
        })

def formtitle(request):
    return request.POST.get('base-title', False)
def formdesc(request):
    return request.POST.get('base-description', False)
def forming(request):
    return request.POST.get('ing-name', False)
def formingamount(request):
    return request.POST.get('ing-amount', False)
def formdir(request):
    return request.POST.get('dir-text', False)
def formnutcal(request):
    return request.POST.get('nut-calories', False)
def formnutfat(request):
    return request.POST.get('nut-fat', False)
def formnutcarbs(request):
    return request.POST.get('nut-carbs', False)
def formnutpro(request):
    return request.POST.get('nut-protein', False)
def formnutchol(request):
    return request.POST.get('nut-cholesterol', False)
def formnutsod(request):
    return request.POST.get('nut-sodium', False)

def getRecipeTitle(request):
    return request.session.get('recipetitle', '')

def checkSessionRecipe(request):
    ingredients = request.session.get('ingredients', [])
    directions = request.session.get('directions', [])
    recipe = request.session.get('recipe', Recipe())
    nutrition = request.session.get('nutrition', Nutrition())

def resetSessionRecipe(request):
    request.session['recipetitle'] = 'def'
    request.session['recipedesc'] = ''
    request.session['ingredients'] = []
    request.session['directions'] = []
    request.session['nutrition'] = []
