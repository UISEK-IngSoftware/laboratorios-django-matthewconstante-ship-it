from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api'

# 1. Creamos el router automático de Django Rest Framework
router = DefaultRouter()

# 2. Registramos tu ViewSet. Esto creará todas las rutas de golpe (/api/, /api/1/, etc.)
router.register(r'pokemons', views.PokemonViewsSet)

urlpatterns = [
    path('', include(router.urls)),
]