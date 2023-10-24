from django.urls import path

# import des views par défaut du système d'authentification
# de django, qui sera renommé auth_views
from django.contrib.auth import views as auth_views

# import des views d'applicompte
from applicompte import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'applicompte/login.html'), name = 'login'),
    path('logout/', views.deconnexion, name = 'logout'),
    path('connexion/', views.connexion),
]