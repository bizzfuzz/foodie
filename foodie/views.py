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
from django.core.files.storage import FileSystemStorage

# Create your views here.
def recipeList(request):
    recipes = Recipe.objects.filter(publishDate__lte =  timezone.now()).order_by('publishDate')
    return render(request, 'foodie/recipeList.html', {'recipes': recipes})

def recipeInfo(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = Ingredient.objects.filter(recipe__pk = recipe.pk)
    directions = Direction.objects.filter(recipe__pk = recipe.pk).order_by('number')
    nutrition = Nutrition.objects.filter(recipe__pk = recipe.pk)
    return render(request, 'foodie/recipeInfo.html',
    {
        'recipe': recipe, 'ingredients': ingredients,
        'directions': directions, 'nut': nutrition
    })

def newRecipe(request):
    if request.method == 'POST':
        if request.POST.get('clear'):
            clearRecipe(request)
        elif request.POST.get('clearing'):
            request.session['ingredients'] = []
        elif request.POST.get('cleardir'):
            request.session['directions'] = []
        elif request.POST.get('publish'):
            recipe = Recipe()
            recipe.title = request.session['title']
            recipe.description = request.session['description']

            ings = request.session['ingredients']
            ingredients = []
            for ing in ings:
                newing = Ingredient()
                newing.amount = ing['amount']
                newing.name = ing['name']
                ingredients.append(newing)

            dirs = request.session['directions']
            directions = []
            for dir in dirs:
                newdir = Direction()
                newdir.number = dirs['number']
                newdir.text = dirs['text']
                directions.append(newdir)

            nutrition = Nutrition()
            nutrition.calories = request.session['calories']
            nutrition.fat = request.session['fat']
            nutrition.carbs = request.session['carbs']
            nutrition.protein = request.session['protein']
            nutrition.cholesterol = request.session['cholesterol']
            nutrition.sodium = request.session['sodium']
        else:
            recipe = parseRecipe(request)
            debugrecipe(recipe)
            processprecipe(request, recipe)
        return redirect('newRecipe')
    else:
        base = RecipeForm(prefix = 'base')
        ing = IngredientForm(prefix = 'ing')
        dir = DirectionForm(prefix = 'dir')
        nut = NutritionForm(prefix = 'nut')
        return render(request, 'foodie/recipeEdit.html',
        {
            'base': base, 'ing': ing, 'dir': dir, 'nut': nut,
            'request': request
        })

def parseRecipe(request):
    ret = {}
    ret['title'] = formtitle(request)
    ret['desc'] = formdesc(request)
    ret['ingredient'] = forming(request)
    ret['ingamount'] = formingamount(request)
    ret['direction'] = formdir(request)
    ret['calories'] = formnutcal(request)
    ret['fat'] = formnutfat(request)
    ret['carbs'] = formnutcarbs(request)
    ret['protein'] = formnutpro(request)
    ret['cholesterol'] = formnutchol(request)
    ret['sodium'] = formnutsod(request)
    return ret

def processprecipe(request, recipe):
    if(recipe['title']):
        request.session['title'] = recipe['title']
    if(recipe['desc']):
        request.session['description'] = recipe['desc']
    if(recipe['ingredient'] and recipe['ingamount']):
        ingredients = request.session.get('ingredients', [])
        newing = {}
        newing['name'] = recipe['ingredient']
        newing['amount'] = recipe['ingamount']
        ingredients.append(newing)
        request.session['ingredients'] = ingredients
    if(recipe['direction']):
        directions = request.session.get('directions', [])
        newdir = {}
        newdir['number'] = len(directions) + 1
        newdir['text'] = recipe['direction']
        directions.append(newdir)
        request.session['directions'] = directions
        #print("dirlen: " + str(len(directions)))
    if(recipe['calories']):
        request.session['calories'] = recipe['calories']
    if(recipe['fat']):
        request.session['fat'] = recipe['fat']
    if(recipe['carbs']):
        request.session['carbs'] = recipe['carbs']
    if(recipe['protein']):
        request.session['protein'] = recipe['protein']
    if(recipe['cholesterol']):
        request.session['cholesterol'] = recipe['cholesterol']
    if(recipe['sodium']):
        request.session['sodium'] = recipe['sodium']

def debugrecipe(recipe):
    print("title: " + str(recipe['title']))
    print("desc: " + str(recipe['desc']))
    print("ing: " + str(recipe['ingredient']))
    print("ingamount: " + str(recipe['ingamount']))
    print("dir: " + str(recipe['direction']))
    print("calories: " + str(recipe['calories']))
    print("fat: " + str(recipe['fat']))
    print("carbs: " + str(recipe['carbs']))
    print("pro: " + str(recipe['protein']))
    print("cholesterol: " + str(recipe['cholesterol']))
    print("sodium: " + str(recipe['sodium']))

def clearRecipe(request):
    request.session['title'] = ''
    request.session['description'] = ''
    request.session['ingredients'] = []
    request.session['directions'] = []
    request.session['calories'] = ''
    request.session['fat'] = ''
    request.session['carbs'] = ''
    request.session['protein'] = ''
    request.session['cholesterol'] = ''
    request.session['sodium'] = ''

def formtitle(request):
    return request.POST.get('pic', False)
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
