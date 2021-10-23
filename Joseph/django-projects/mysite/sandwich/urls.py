from django.urls import path
from . import views

urlpatterns = [
    # sandwich homepage
    # http://127.0.0.1:8000/sandwich
    path('', views.sandwich, name='sandwich'),
    # ingredients routes
    # http://127.0.0.1:8000/sandwich/ingredients/<str:ingredient_type>
    path('ingredients/<str:ingredient_type>',
         views.ingredients_list, name='ingredients_list'),
    # random sandwich generator
    # http://127.0.0.1:8000/sandwich/random
    path('random', views.sandwich_generator, name='sandwich_generator'),
    # sandwich menu
    # http://127.0.0.1:8000/sandwich/menu
    path('menu', views.sandwich_menu, name='sandwich_menu')
]
