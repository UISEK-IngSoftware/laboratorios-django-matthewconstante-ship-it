from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        # Usamos '__all__' para incluir todos los campos del modelo
        fields = '__all__'
        
        # Aquí personalizamos los nombres que verá el usuario
        labels = {
            'name': 'Nombre',
            'type': 'Tipo de Pokémon',
            'height': 'Altura (m)',
            'weight': 'Peso (kg)',
            'description': 'Descripción / Bio',
            'trainer': 'Entrenador asignado',
            'picture': 'Foto del Pokémon',
      }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-0 bg-light', 'placeholder': 'Ej. Charizard'}),
            'type': forms.Select(attrs={'class': 'form-select border-0 bg-light'}),
            'height': forms.NumberInput(attrs={'class': 'form-control border-0 bg-light', 'step': '0.01'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control border-0 bg-light', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control border-0 bg-light', 'rows': 3, 'placeholder': 'Describe sus habilidades...'}),
            'trainer': forms.Select(attrs={'class': 'form-select border-0 bg-light'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control border-0  bg-light'}),
        }