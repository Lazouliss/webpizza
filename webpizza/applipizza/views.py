from django.shortcuts import render

# import des modèles
from applipizza.models import Pizza, Ingredient, Composition

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

    # on retourne l'emplacement du template et de la pizza récup dans la base de données
    return render(
        request,
        'applipizza/pizza.html',
        {'pizza' : laPizza,
         'compo' : laCompo}
    )