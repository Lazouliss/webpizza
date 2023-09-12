from django.db import models

# Create your models here.

class Ingredient(models.Model) :

    # idIngredient est une clé primaire, n auto-increment => AutoField
    idIngredient = models.AutoField(primary_key = True)

    # nomIngredient est une chaine de caractère = CharField
    nomIngredient = models.CharField(max_length = 50, verbose_name = 'le nom de cet ingrédient')

    # une mthode de type 'toString'
    def __str__(self) -> str :
        return self.nomIngredient
    
class Pizza(models.Model) :

    # idPizza est une clé primaire, n auto-increment => AutoField
    idPizza = models.AutoField(primary_key = True)

    # nomPizza est une chaine de caractère = CharField
    nomPizza = models.CharField(max_length = 50, verbose_name = 'le nom de cette pizza')
    
    # le prix est décimal, maximum = 4 chiffres, dont 2 décimales
    prix = models.DecimalField(max_digits = 4, decimal_places = 2, verbose_name = 'le prix')

    # une mthode de type 'toString'
    def __str__(self) -> str :
        return 'pizza' + self.nomPizza + ' (prix : ' + str(self.prix) + ' €)'

    
