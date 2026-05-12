from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render, get_object_or_404 
from pokedex.forms import PokemonForm

def index(request):
    pokemons = Pokemon.objects.all()
    trainers_list = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'Trainers': trainers_list
    }, request))

def pokemon(request, id):
    pokemon_obj = get_object_or_404(Pokemon, id=id)
    template = loader.get_template('display_pokemon.html')
    context = {'pokemon': pokemon_obj}
    return HttpResponse(template.render(context, request))

def trainer_details(request, id):
    trainer_obj = get_object_or_404(Trainer, id=id)
    template = loader.get_template('display_trainer.html')
    context = {'trainer': trainer_obj}
    return HttpResponse(template.render(context, request))

def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('pokedex:index') 
    else:
        form = PokemonForm()
    return render(request, 'add_pokemon.html', {'form': form})

def edit_pokemon(request, id): 
    pokemon_obj = get_object_or_404(Pokemon, id=id) 
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon_obj)
        if form.is_valid():
            form.save() 
            return redirect('pokedex:index') 
    else:
        form = PokemonForm(instance=pokemon_obj)
    
    return render(request, 'pokemon_form.html', {'form': form})

def delete_pokemon(request, id):
    pokemon_obj = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        pokemon_obj.delete()
        return redirect('pokedex:index')
    
    # Si entran por GET (URL directa), los mandamos al detalle para que usen el botón
    return redirect('pokedex:pokemon', id=id)