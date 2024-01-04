from django.shortcuts import render
from .models import Fournisseur



# Create your views here.

def inv_magasin(request):
    return render(request, 'inv_magasin.html')





def ajouter_fournisseur(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom_fournisseur = request.POST.get('nom_fournisseur')
        # Ajouter le fournisseur à la base de données
        fournisseur = Fournisseur.objects.create(nom_fournisseur=nom_fournisseur)
        # Rediriger ou afficher un message de succès
    else:
        # Afficher le formulaire pour ajouter un fournisseur
        return render(request, 'ajouter_fournisseur.html')

# Note: Vous devrez créer un template HTML (ajouter_fournisseur.html) pour afficher le formulaire.on le fais dans un seul fichier 

