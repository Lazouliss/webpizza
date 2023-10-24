from django.contrib import admin

# Register your models here.
# admin password : Azerty.123
# staff : staff123
from applipizza.models import Ingredient, Pizza, Composition
admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Composition)