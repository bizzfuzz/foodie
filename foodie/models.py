from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200, null=True, blank=True)
    publishDate = models.DateTimeField(blank = True, null = True)
    description = models.TextField(null=True, blank=True)

    def publish(self):
        self.publishDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    amount = models.CharField(max_length = 100, null=True, blank=True)
    name = models.CharField(max_length = 100, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

class Direction(models.Model):
    number = models.IntegerField()
    text = models.TextField(null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

class Nutrition(models.Model):
    calories = models.IntegerField(null=True, blank=True)
    fat = models.DecimalField(max_digits = 10, decimal_places = 1, null=True, blank=True)
    carbs = models.DecimalField(max_digits = 10, decimal_places = 1, null=True, blank=True)
    protein = models.DecimalField(max_digits = 10, decimal_places = 1, null=True, blank=True)
    cholesterol = models.IntegerField(null=True, blank=True)
    sodium = models.IntegerField(null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
