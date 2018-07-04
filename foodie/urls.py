from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recipeList, name = "recipeList"),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipeInfo, name = 'recipeInfo'),
    url(r'^recipe/new/', views.newRecipe, name = 'newRecipe'),
]
