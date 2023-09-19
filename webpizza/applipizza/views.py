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