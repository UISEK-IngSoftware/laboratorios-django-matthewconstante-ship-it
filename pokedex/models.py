from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    POKEMON_TIPES = {
        ("Agua", "Agua"),
        ("Fuego", "Fuego"),
        ("Tierra", "Tierra"),
        ("Electrico", "Electrico"),
        ("Planta", "Planta"),
        ("Volador", "Volador"),
        ("Roca", "Roca"),
        ("Hielo", "Hielo"),
        ("Dragon", "Dragon"),
        ("Sombra", "Sombra"),
        ("Normal", "Normal"),
        ("Fantasma", "Fantasma"),
        ("Lucha", "Lucha"),
        ("Psiquico", "Psiquico"),
        ("Bicho", "Bicho"),
        ("Hada", "Hada"),
        ("Acero", "Acero"),
        ("Veneno", "Veneno"),
    }
    type = models.CharField(max_length=50 , choices=POKEMON_TIPES, null=False)
    height = models.DecimalField(decimal_places=4, max_digits=10)
    weight = models.DecimalField(decimal_places=4, max_digits=10)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, related_name='pokemons')
    def __str__(self):
        return self.name
    

# Create your models here.
