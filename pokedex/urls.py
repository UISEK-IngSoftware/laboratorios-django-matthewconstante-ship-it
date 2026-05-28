from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "pokedex"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name='login_directo.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    path("pokemon/add/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:id>/", views.delete_pokemon, name="delete_pokemon"),
    path("Trainer/<int:id>/", views.trainer_details, name="Trainer"),
    path("trainer/add/", views.add_trainer, name="add_trainer"),
    path("edit_trainer/<int:id>/", views.edit_trainer, name="edit_trainer"),
    path("delete_trainer/<int:id>/", views.delete_trainer, name="delete_trainer"),
]