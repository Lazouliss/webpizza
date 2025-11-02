# WebPizza 🍕

WebPizza est une application web de commande de pizzas développée avec Django 4.2. Cette application permet aux utilisateurs de commander des pizzas en ligne, de gérer leur compte et leur panier d'achats.

L'objectif du projet était d'apprendre à développer une application avec Django et de faire l'usage de templates pour créer les pages.

## Note importante

⚠️ Cette application a été développée dans le cadre d'un projet d'IUT et certaines fonctionnalités peuvent nécessiter l'accès au serveur de l'IUT qui n'est pas accessible publiquement. Des modifications peuvent être nécessaires pour finir de lancer l'application.

Tout a été developpé jusqu'au tp 16 inclus.

## Structure du Projet

Le projet est organisé en trois applications Django principales :

### 1. `applipizza/`
- Gestion du catalogue des pizzas
- Création et modification des pizzas
- Gestion des ingrédients
- Templates pour l'affichage des pizzas et des formulaires

### 2. `applicompte/`
- Gestion des comptes utilisateurs
- Authentification (login/logout)
- Profils utilisateurs
- Réinitialisation de mot de passe
- Différents menus selon le type d'utilisateur (client/staff)

### 3. `applipanier/`
- Gestion du panier d'achats
- Traitement des commandes
- Historique des commandes
- Système de paiement

## Organisation des fichiers

```
webpizza/
├── manage.py
├── webpizza/               # Configuration principale
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── applipizza/             # Application de gestion des pizzas
├── applicompte/            # Application de gestion des comptes
├── applipanier/            # Application de gestion du panier
└── images/                 # Stockage des images
    ├── imagesPizzas/
    └── imagesUsers/
```

## Configuration requise

- Python 3.x
- Django 4.2
- SQLite3 (base de données incluse)

## Installation et lancement

1. Cloner le repository :
```bash
git clone https://github.com/Lazouliss/webpizza.git
cd webpizza
```

2. Créer un environnement virtuel Python et l'activer :
```bash
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur Linux/Mac
source venv/bin/activate
```

3. Installer les dépendances :
```bash
pip install django
```

4. Appliquer les migrations :
```bash
python manage.py migrate
```

5. Lancer le serveur de développement :
```bash
python manage.py runserver
```

L'application sera accessible à l'adresse http://127.0.0.1:8000/pizzas/

## Fonctionnalités principales

- 🍕 Catalogue de pizzas avec images
- 👤 Gestion des comptes utilisateurs
- 🛒 Panier d'achats
- 💳 Système de commande
- 👨‍🍳 Interface d'administration pour le staff
- 📱 Interface responsive
- 🔑 Système de réinitialisation de mot de passe

## Identifiants et mot de passes des utilisateurs de test

L'utilisateur **admin** permet seulement de se connecter à l'interface d'administration de Django (accessible à l'adresse http://127.0.0.1:8000/admin/)

| Identifiant | Mot de passe | Superuser |
| --------  | ------------- | --------- |
| admin     | admin         | oui       |
| claudio   | webpizza1234  | non       |
| pablo     | webpizza1234  | oui       |
| pedro     | webpizza1234  | non       |
| thomas    | webpizza1234  | non       |
| tmontig   | webpizza1234  | oui       |
