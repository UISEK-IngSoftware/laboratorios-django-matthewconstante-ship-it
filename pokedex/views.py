from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    trainers_list = Trainer.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'Trainers': trainers_list
    }, request))

def pokemon(request, id):
    pokemon_obj = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {'pokemon': pokemon_obj}
    return HttpResponse(template.render(context, request))

def trainer_details(request, id):
    trainer_obj = Trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html')
    context = {'trainer': trainer_obj}
    return HttpResponse(template.render(context, request))
