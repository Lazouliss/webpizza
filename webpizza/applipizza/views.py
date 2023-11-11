from django.shortcuts import render

# import des modèles
from applipizza.models import Pizza, Ingredient, Composition
from applipizza.forms import IngredientForm, PizzaForm, CompositionForm
from django.contrib.auth.models import User
from applicompte.models import PizzaUser

# Create your views here.
def pizzas(request) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)

    # récupération des pizzas de la base de données avec les mêmes instructions que dans le shell
    lesPizzas = Pizza.objects.all()

    # on retourne l'emplacement du template et, même s'il ne pas cette fois, le paramètre request, ainsi que le contenu calculé (lesPizzas) sout forme d'un dictionnaire python
    return render(
        request,
        'applipizza/pizzas.html',
        {'pizzas' : lesPizzas, 'user' : user}
    )

def ingredients(request) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        lesIngredients = Ingredient.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/ingredients.html',
            {'ingredients' : lesIngredients, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def pizza(request, pizza_id) :
    user = None
    if request.user.is_authenticated :
        user = PizzaUser.objects.get(id = request.user.id)

    # récupération de la pizza dont l'id a été passé en paramètre (int:pizza_id)
    laPizza = Pizza.objects.get(idPizza = pizza_id)
    # récupération de la composition de la pizza dont l'id a été passé en paramètre (int:pizza_id)
    laCompo = Composition.objects.filter(pizza = pizza_id)

    lesIngredients = Ingredient.objects.all()

    # on retourne l'emplacement du template et de la pizza récup dans la base de données
    return render(
        request,
        'applipizza/pizza.html',
        {'pizza' : laPizza,
         'compo' : laCompo,
         'lesIng' : lesIngredients,
         'user' : user}
    )

def formulaireCreationIngredient(request) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/formulaireCreationIngredient.html',
            { "user" : user }
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def creerIngredient(request) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        # récupération du formulaire posté
        form = IngredientForm(request.POST)

        if form.is_valid() :
            # récupération de la valeur du champ 'nomIngredient' 
            # form.cleaned_data permet de nettoyer la donnée au cas où des injections en tout genre seraient présentes
            nomIng = form.cleaned_data['nomIngredient']

            # création d'un nouvel ingrédient
            ing = Ingredient()

            # affectation de l'ingrédient dans la base
            ing.nomIngredient = nomIng

            # engregistrement de l'ingrédient dans la base
            ing.save()

        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/traitementFormulaireCreationIngredient.html',
            {"nom" : nomIng, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def formulaireCreationPizza(request) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/formulaireCreationPizza.html',
            { "user" : user }
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def creerPizza(request) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        user = PizzaUser.objects.get(id = request.user.id)
        # récupération du formulaire posté
        form = PizzaForm(request.POST)

        if form.is_valid() :
            # création d'une nouvelle pizza
            piz = Pizza()

            # récupération de la valeur du champ 'nomPizza' 
            # form.cleaned_data permet de nettoyer la donnée au cas où des injections en tout genre seraient présentes
            piz.nomPizza = form.cleaned_data['nomPizza']
            piz.prix = form.cleaned_data['prix']
            piz.image = request.FILES['image']

            # engregistrement de la pizza dans la base
            piz.save()

        # on retourne l'emplacement de la vue (ou plutôt du template, au sens de django) et le contenu calculé, sous forme d'un dictionnaire python
        return render(
            request,
            'applipizza/traitementFormulaireCreationPizza.html',
            { "nom" : piz.nomPizza, "user" : user }
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def ajouterIngredientDansPizza(request, pizza_id) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        # récupération du formulaire posté
        formulaire = CompositionForm(request.POST)

        if formulaire.is_valid() :
            # récupération de la valeur du champ 'nomPizza' 
            # form.cleaned_data permet de nettoyer la donnée au cas où des injections en tout genre seraient présentes
            ing = formulaire.cleaned_data['ingredient']
            qte = formulaire.cleaned_data['quantite']
            piz = Pizza.objects.get(idPizza = pizza_id)
            compoPizza = Composition.objects.filter(pizza = pizza_id)
            lesIngredientsDeLaPizza = ((ligne.ingredient) for ligne in compoPizza)

            if ing in lesIngredientsDeLaPizza :
                compo = Composition.objects.filter(pizza = pizza_id, ingredient = ing)
                compo.delete()

            # création de la nouvelle instance de Composition et remplissage des attributs
            compo = Composition()
            compo.ingredient = ing
            compo.pizza = piz
            compo.quantite = qte
            # sauvegrade dans la base de la composition
            compo.save()

        # recupération de tous les ingrédients pour construire le futur select
        lesIngredients = Ingredient.objects.all()
        # actualisation des ingrédeitns entrant dans la composition de la pizza
        compoPizza = Composition.objects.filter(pizza = pizza_id)
        # on crée une liste dont chaque item contiendra l'identifiant de la composition (idComposition),
        # le nom de l'ingrédient et la quantité del i'ngrédeint dans cette composition
        listeIngredients = []
        for ligneCompo in compoPizza :
            # on récupère l'Ingredient pour utiliser son nomIngredient
            ingredient = Ingredient.objects.get(idIngredient = ligneCompo.ingredient.idIngredient)
            listeIngredients.append(
                {"idComposition" : ligneCompo.idComposition, "nom" : ingredient.nomIngredient, "qte" : ligneCompo.quantite}
            )
        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/pizza.html',
            {"pizza" : piz, "liste" : listeIngredients, "compo" : compoPizza, "lesIng" : lesIngredients, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def supprimerPizza(request, pizza_id) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        # récupération de la pizza dont l'id a été passé en paramètre (int:pizza_id)
        laPizza = Pizza.objects.get(idPizza = pizza_id)
        # suppression de la pizza
        laPizza.delete()

        # récupération des pizzas de la base de données avec les mêmes instructions que dans le shell
        lesPizzas = Pizza.objects.all()

        # on retourne l'emplacement du template et, même s'il ne pas cette fois, le paramètre request, ainsi que le contenu calculé (lesPizzas) sous forme d'un dictionnaire python
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/formulaireCreationIngredient.html',
            {'pizzas' : lesPizzas, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def afficherFormulaireModificationPizza(request, pizza_id) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        # récupération de la pizza dont l'id a été passé en paramètre (int:pizza_id)
        pizza_a_modifier = Pizza.objects.get(idPizza = pizza_id)
        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/formulaireModificationPizza.html',
            { 'pizza' : pizza_a_modifier, "user" : user }
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def modifierPizza(request, pizza_id) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        # récupération de la pizza dont l'id a été passé en paramètre (int:pizza_id)
        laPizza = Pizza.objects.get(idPizza = pizza_id)
        
        # récupération du formulaire posté
        form = PizzaForm(request.POST, request.FILES, instance = laPizza)

        if form.is_valid() :
            if 'image' in request.FILES:
                laPizza.image = request.FILES['image']
            form.save()
            laPizza.save()
        
        laPizza = Pizza.objects.get(idPizza = pizza_id)

        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/traitementFormulaireModificationPizza.html',
            {'nom' : laPizza.nomPizza, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def supprimerIngredient(request, ingredient_id) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        # récupération de l'ingredient dont l'id a été passé en paramètre (int:ingredient_id)
        laIngredient = Ingredient.objects.get(idIngredient = ingredient_id)
        # suppression de la ingredient
        laIngredient.delete()

        # récupération des ingredients de la base de données avec les mêmes instructions que dans le shell
        lesIngredients = Ingredient.objects.all()

        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/ingredients.html',
            {'ingredients' : lesIngredients, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def afficherFormulaireModificationIngredient(request, ingredient_id) :
        # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        user = PizzaUser.objects.get(id = request.user.id)
        # récupération de l'ingredient dont l'id a été passé en paramètre (int:ingredient_id)
        ingredient_a_modifier = Ingredient.objects.get(idIngredient = ingredient_id)
        return render(
            request,
            'applipizza/formulaireModificationIngredient.html',
            {'ingredient' : ingredient_a_modifier, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )
    
    # récupération de l'ingredient dont l'id a été passé en paramètre (int:ingredient_id)
    ingredient_a_modifier = Ingredient.objects.get(idIngredient = ingredient_id)
    return render(
        request,
        'applipizza/formulaireModificationIngredient.html',
        {'ingredient' : ingredient_a_modifier}
    )

def modifierIngredient(request, ingredient_id) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        # récupération de l'ingredient dont l'id a été passé en paramètre (int:ingredient_id)
        unIngredient = Ingredient.objects.get(idIngredient = ingredient_id)
        
        # récupération du formulaire posté
        form = IngredientForm(request.POST, instance = unIngredient)

        if form.is_valid() :
            form.save()

        ing = Ingredient.objects.get(idIngredient = ingredient_id)

        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/traitementFormulaireModificationIngredient.html',
            {'nom' : ing.nomIngredient, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )

def supprimerIngredientDansPizza(request, pizza_id, composition_id) :
    # création du user
    user = None

    # cas d'un utilisateur staff
    if request.user.is_staff :
        # récupération de la composition dont l'id a été passé en paramètre (int:ingredient_id)
        laComposition = Composition.objects.get(idComposition = composition_id)
        # suppression de la composition
        laComposition.delete()
        
        # récupération des pizzas
        lesPizzas = Pizza.objects.all()

        user = PizzaUser.objects.get(id = request.user.id)
        # on retourne l'emplacement du template
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )

    # cas d'un client connecté
    elif request.user.is_authenticated :
        lesPizzas = Pizza.objects.all()
        user = PizzaUser.objects.get(id = request.user.id)
        return render(
            request,
            'applipizza/pizzas.html',
            {'pizzas' : lesPizzas, "user" : user}
        )
    
    # cas d'un internaute non connecté
    else :
        return render(
            request,
            'applicompte/login.html',
        )