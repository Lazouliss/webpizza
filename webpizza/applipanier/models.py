from django.db import models

from applicompte.models import PizzaUser
from applipizza.models import Pizza

# Create your models here.
class Commande(models.Model) :
    idCommande = models.AutoField(primary_key = True)
    dateCommande = models.DateField(verbose_name='date de passage de la commande')
    payee = models.BooleanField(verbose_name='commande payee ?')
    prix = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='prix total')
    # une seule clé -> pas besoin de tester l'unicité
    pizzauser = models.ForeignKey(PizzaUser, on_delete=models.CASCADE)

class LigneCommande(models.Model) :
    idLigneCommande = models.AutoField(primary_key = True)
    quantite = models.IntegerField(verbose_name='nombre de pizza(s)')
    prix = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name='prix total')

    # deux clés -> test unicité 2 à 2
    class Meta :
        unique_together = ('commande', 'pizza')
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)