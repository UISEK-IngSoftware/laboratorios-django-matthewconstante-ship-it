from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons, 'Trainers': trainers})

def pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})

def trainer_details(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    return render(request, 'display_trainer.html', {'trainer': trainer})

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, id):
    obj = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=obj)
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, id):
    obj = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        obj.delete()
    return redirect('pokedex:index')

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer(request, id):
    obj = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = TrainerForm(instance=obj)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, id):
    obj = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        obj.delete()
    return redirect('pokedex:index')