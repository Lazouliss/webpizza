from django.urls import path

# import des views d'applicompte
from applipanier import views

urlpatterns = [
    path('cart/', views.afficherPanier),
    path('pizzas/<int:pizza_id>/buy/', views.ajouterPizzaAuPanier),
    path('cart/<int:pizza_id>/delete/', views.retirerDuPanier),
    path('cart/delete/', views.viderPanier),
    path('cart/<int:pizza_id>/decrease/', views.retirerUnePizzaDuPanier),
    path('cart/pay/', views.payerPanier),
    path('orders/', views.afficherCommandes),
    path('orders/<int:order_id>/', views.afficherDetailsCommande),
]