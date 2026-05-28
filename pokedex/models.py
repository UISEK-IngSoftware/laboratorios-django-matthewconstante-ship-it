from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='trainer_images', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=20, null=False)
    height = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    description = models.TextField(blank=True, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=False)
    picture = models.ImageField(upload_to='pokemon_images', null=True, blank=True)

    def __str__(self):
        return self.name