from rest_framework import viewsets
from pokedex.models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewsSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    