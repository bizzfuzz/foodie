from django import forms
from .models import Recipe
from .models import Ingredient
from .models import Direction
from .models import Nutrition

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'image')

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('amount', 'name',)

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ('text',)

class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ('calories', 'fat', 'carbs', 'protein', 'cholesterol', 'sodium',)
