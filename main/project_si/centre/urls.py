from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('produits/',views.liste_produits, name='listeP'),
    path('produits/ajouter',views.ajouter_produit, name='ajouterP'),
    path('produits/supprimer/<int:pid>/',views.supprimer_produit, name='supprimerP'),
    path('produits/modifier/<int:pid>/',views.modifier_produit, name='modifierP'),
    path('centre/<int:cid>',views.centre1, name='centre1'),
]