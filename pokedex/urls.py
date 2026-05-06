from django.urls import path
from . import views

urlpatterns = [
    # Inicio: http://127.0.0.1:8000/
    path("", views.index, name="index"),
    
    # Detalle Pokémon: http://127.0.0.1:8000/pokemon/1/
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    
    # Detalle Entrenador: http://127.0.0.1:8000/Trainer/1/
    path("Trainer/<int:id>/", views.trainer_details, name="Trainer"),
]