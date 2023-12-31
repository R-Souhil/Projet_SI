from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produit


# Create your views here.

def ajouter_produit(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom_produit = request.POST.get('nom_produit')
        # Ajouter le produit à la base de données
        produit = Produit.objects.create(nom_produit=nom_produit)
        # Rediriger ou afficher un message de succès
    else:
        # Afficher le formulaire pour ajouter un produit
        return render(request, 'ajouter_produit.html')

# Note: Vous devrez créer un template HTML (ajouter_produit.html) pour afficher le formulaire.

def rechercher_produit(request):
    if request.method == 'GET':
        # Récupérer le nom du produit à rechercher depuis la requête
        nom_produit = request.GET.get('nom_produit')
        # Effectuer la recherche dans la base de données
        produits = Produit.objects.filter(nom_produit__icontains=nom_produit)
        # Afficher les résultats ou rediriger vers une page de résultats
    else:
        # Afficher un formulaire de recherche
        return render(request, 'rechercher_produit.html')

# Note: Vous devrez créer un template HTML (rechercher_produit.html) pour afficher le formulaire de recherche.


def supprimer_produit(request, produit_id):
    # Récupérer le produit à supprimer
    produit = get_object_or_404(Produit, pk=produit_id)
    
    # Supprimer le produit
    produit.delete()

    # Rediriger ou afficher un message de succès

