from django import forms
from .models import Pokemon, Trainer
class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        

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
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control border-0 bg-light'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            'first_name': 'Nombre(s)',
            'last_name': 'Apellido(s)',
            'level': 'Nivel de Entrenador',
            'birth_date': 'Fecha de Nacimiento',
            'picture': 'Foto de Perfil',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control border-0 bg-light', 'placeholder': 'Ej. Ash'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control border-0 bg-light', 'placeholder': 'Ej. Ketchum'}),
            'level': forms.NumberInput(attrs={'class': 'form-control border-0 bg-light', 'placeholder': 'Ej. 10'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control border-0 bg-light', 'type': 'date'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control border-0 bg-light'}),
        }