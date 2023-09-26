from django.shortcuts import render

# import des modèles
from applipizza.models import Pizza, Ingredient, Composition
from applipizza.forms import IngredientForm, PizzaForm

# Create your views here.
def pizzas(request) :
    # récupération des pizzas de la base de données avec les mêmes instructions que dans le shell
    lesPizzas = Pizza.objects.all()

    # on retourne l'emplacement du template et, même s'il ne pas cette fois, le paramètre request, ainsi que le contenu calculé (lesPizzas) sout forme d'un dictionnaire python
    return render(
        request,
        'applipizza/pizzas.html',
        {'pizzas' : lesPizzas}
    )

def ingredients(request) :
    # récupération des ingredients de la base de données avec les mêmes instructions que dans le shell
    lesIngredients = Ingredient.objects.all()

    # on retourne l'emplacement du template et, même s'il ne pas cette fois, le paramètre request, ainsi que le contenu calculé (lesIngredients) sout forme d'un dictionnaire python
    return render(
        request,
        'applipizza/ingredients.html',
        {'ingredients' : lesIngredients}
    )

def pizza(request, pizza_id) :
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
         'lesIng' : lesIngredients}
    )

def formulaireCreationIngredient(request) :
    # on retourne l'emplacement du template
    return render(
        request,
        'applipizza/formulaireCreationIngredient.html'
    )

def creerIngredient(request) :
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

        # on retourne l'emplacement de la vue (ou plutôt du template, au sens de django) et le contenu calculé, sous forme d'un dictionnaire python
    
    return render(
        request,
        'applipizza/traitementFormulaireCreationIngredient.html',
        {"nom" : nomIng}
    )

def formulaireCreationPizza(request) :
    # on retourne l'emplacement du template
    return render(
        request,
        'applipizza/formulaireCreationPizza.html'
    )

def creerPizza(request) :
    # récupération du formulaire posté
    form = PizzaForm(request.POST)

    if form.is_valid() :
        # récupération de la valeur du champ 'nomPizza' 
        # form.cleaned_data permet de nettoyer la donnée au cas où des injections en tout genre seraient présentes
        nomPiz = form.cleaned_data['nomPizza']
        prixPiz = form.cleaned_data['prix']

        # création d'une nouvelle pizza
        piz = Pizza()

        # affectation de la pizza dans la base
        piz.nomPizza = nomPiz
        piz.prix = prixPiz

        # engregistrement de la pizza dans la base
        piz.save()

        # on retourne l'emplacement de la vue (ou plutôt du template, au sens de django) et le contenu calculé, sous forme d'un dictionnaire python
    
    return render(
        request,
        'applipizza/traitementFormulaireCreationPizza.html',
        {"nom" : nomPiz}
    )
