from django.contrib import admin

# Register your models here.
# admin : Admin.123
# staff : staff123
# user : users123
from applipizza.models import Ingredient, Pizza, Composition
admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Composition)