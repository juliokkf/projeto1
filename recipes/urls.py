
from django.urls import path
from recipes.views import home
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"), #Home
    path('recipes/category/<int:category_id>/', views.category, name="category"), 
    path('recipes/<int:id>/', views.recipe, name="recipe"), #Home    
]
