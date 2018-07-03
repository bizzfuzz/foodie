from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    publishDate = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.publishDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    amount = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

class Direction(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
