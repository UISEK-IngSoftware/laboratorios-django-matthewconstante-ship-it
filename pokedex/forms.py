from django import forms
from .models import Pokemon, Trainer

# LISTA OFICIAL DE TIPOS PARA EL DESPLEGABLE
POKEMON_TYPES = [
    ('Agua', 'Agua'),
    ('Acero', 'Acero'),
    ('Bicho', 'Bicho'),
    ('Dragón', 'Dragón'),
    ('Eléctrico', 'Eléctrico'),
    ('Fantasma', 'Fantasma'),
    ('Fuego', 'Fuego'),
    ('Hada', 'Hada'),
    ('Hielo', 'Hielo'),
    ('Lucha', 'Lucha'),
    ('Normal', 'Normal'),
    ('Planta', 'Planta'),
    ('Psíquico', 'Psíquico'),
    ('Roca', 'Roca'),
    ('Siniestro', 'Siniestro'),
    ('Tierra', 'Tierra'),
    ('Veneno', 'Veneno'),
    ('Volador', 'Volador'),
]

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-0 bg-light', 'id': 'id_name'}),
            # Vinculamos la lista de tipos aquí:
            'type': forms.Select(choices=POKEMON_TYPES, attrs={'class': 'form-select border-0 bg-light', 'id': 'id_type'}),
            'height': forms.NumberInput(attrs={'class': 'form-control border-0 bg-light', 'id': 'id_height', 'step': '0.01'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control border-0 bg-light', 'id': 'id_weight', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control border-0 bg-light', 'id': 'id_description', 'rows': 3}),
            'trainer': forms.Select(attrs={'class': 'form-select border-0 bg-light'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control border-0 bg-light', 'id': 'id_picture'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control border-0 bg-light'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control border-0 bg-light'}),
            'level': forms.NumberInput(attrs={'class': 'form-control border-0 bg-light'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control border-0 bg-light', 'type': 'date'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control border-0 bg-light'}),
        }