from django.shortcuts import render

from applicompte.models import PizzaUser
from applipanier.models import Commande, LigneCommande
from applipizza.models import Pizza
from datetime import datetime

# Create your views here.
def afficherPanier(request) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)
        lesCommandesNonPayees = Commande.objects.filter(pizzauser = user).filter(payee = False)
        if lesCommandesNonPayees :
            panier = lesCommandesNonPayees[0]
            lesLignesDuPanier = LigneCommande.objects.filter(commande_id = panier.idCommande)
        else :
            panier = None
            lesLignesDuPanier = None
        
        return render(
            request,
            'applipanier/panier.html',
            {"user" : user, "panier" : panier, "lignesPanier" : lesLignesDuPanier}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )
    
def ajouterPizzaAuPanier(request, pizza_id) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)
        # piz à ajouter
        piz = Pizza.objects.get(idPizza = pizza_id)
        # récup panier ou crée panier si inexistant
        lesCommandesNonPayees = Commande.objects.filter(pizzauser = user).filter(payee = False)
        if lesCommandesNonPayees :
            panier = lesCommandesNonPayees[0]
        else:
            panier = Commande()
            panier.dateCommande = datetime.today().strftime('%Y-%m-%d')
            panier.payee = 0
            panier.prix = 0
            panier.pizzauser = user

        # ajoute prix piz
        panier.prix += piz.prix
        panier.save()
        # modifie LigneCommande relative à piz
        lignePizza = LigneCommande.objects.filter(commande_id = panier.idCommande).filter(pizza = piz)
        if lignePizza :
            lignePizza = lignePizza[0]
            lignePizza.quantite += 1
            lignePizza.prix += piz.prix
        else:
            lignePizza = LigneCommande()
            lignePizza.pizza = piz
            lignePizza.quantite = 1
            lignePizza.prix = piz.prix
            lignePizza.commande = panier
        lignePizza.save()
        # actualise le panier
        lesLignesDuPanier = LigneCommande.objects.filter(commande_id = panier.idCommande)
        return render(
            request,
            'applipanier/panier.html',
            {"user" : user, "panier" : panier, "lignesPanier" : lesLignesDuPanier}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )

def retirerDuPanier(request, pizza_id) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)
        # piz à retirer
        piz = Pizza.objects.get(idPizza = pizza_id)
        # récup panier
        lesCommandesNonPayees = Commande.objects.filter(pizzauser = user).filter(payee = False)
        if lesCommandesNonPayees :
            panier = lesCommandesNonPayees[0]

            # modifie LigneCommande relative à piz
            lignePizza = LigneCommande.objects.filter(commande_id = panier.idCommande).filter(pizza = piz)
            if lignePizza :
                lignePizza = lignePizza[0]
                qtt = lignePizza.quantite
                lignePizza.delete()

            # actualise prix panier
            panier.prix -= qtt*piz.prix
            panier.save()

            # actualise les lignes du panier
            lesLignesDuPanier = LigneCommande.objects.filter(commande_id = panier.idCommande)
            if not lesLignesDuPanier :
                panier.delete()
                panier = None
                lesLignesDuPanier = None

        # en cas d'accès à la page autrement que par le bouton et que le panier n'existe pas
        else :
            panier = None
            lesLignesDuPanier = None

        return render(
            request,
            'applipanier/panier.html',
            {"user" : user, "panier" : panier, "lignesPanier" : lesLignesDuPanier}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )
    
def viderPanier(request) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)

        lesCommandesNonPayees = Commande.objects.filter(pizzauser = user).filter(payee = False)
        panier = lesCommandesNonPayees[0]
        panier.delete()

        panier = None
        lesLignesDuPanier = None
        return render(
            request,
            'applipanier/panier.html',
            {"user" : user, "panier" : panier, "lignesPanier" : lesLignesDuPanier}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )
    
def retirerUnePizzaDuPanier(request, pizza_id) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)
        
        # récup panier
        lesCommandesNonPayees = Commande.objects.filter(pizzauser = user).filter(payee = False)
        if lesCommandesNonPayees :
            panier = lesCommandesNonPayees[0]

        # piz à retirer
        piz = Pizza.objects.get(idPizza = pizza_id)

        # ligne à modifier
        lignePizza = LigneCommande.objects.filter(commande_id = panier.idCommande).filter(pizza = piz)
        if lignePizza :
            lignePizza = lignePizza[0]
            qtt = lignePizza.quantite

        # retirer prix piz
        panier.prix -= piz.prix

        # retirer 1 piz
        if qtt==1 :
            lignePizza.delete()
        else:
            lignePizza.quantite -= 1
            lignePizza.prix -= piz.prix
            lignePizza.save()

        panier.save()

        # actualise le panier
        lesLignesDuPanier = LigneCommande.objects.filter(commande_id = panier.idCommande)
        if not lesLignesDuPanier :
            panier.delete()
            panier = None
            lesLignesDuPanier = None

        return render(
            request,
            'applipanier/panier.html',
            {"user" : user, "panier" : panier, "lignesPanier" : lesLignesDuPanier}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )

def payerPanier(request) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)
        # récup panier
        lesCommandesNonPayees = Commande.objects.filter(pizzauser = user).filter(payee = False)
        if lesCommandesNonPayees :
            panier = lesCommandesNonPayees[0]

        # actualisation de la date
        panier.dateCommande = datetime.today().strftime('%Y-%m-%d')
        panier.payee = True
        panier.save()

        return render(
            request,
            'applipanier/avisPaiement.html',
            {"user" : user, "panier" : panier}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )
    
def afficherCommandes(request) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)
        # récup commandes
        commandes = Commande.objects.filter(pizzauser = user).filter(payee = True)

        return render(
            request,
            'applipanier/commandes.html',
            {"user" : user, "commandes" : commandes}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )
    
def afficherDetailsCommande(request, order_id) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)
        # récup commande        
        laCommande = Commande.objects.filter(pizzauser = user).filter(idCommande = order_id)
        commande = laCommande[0]
        # récup détails de la commande
        lesLignesDeLaCommande = LigneCommande.objects.filter(commande_id = commande.idCommande)
        
        return render(
            request,
            'applipanier/commande.html',
            {"user" : user, "commande" : commande, "lignesCommande" : lesLignesDeLaCommande}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )