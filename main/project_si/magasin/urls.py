from django.urls import path
from magasin import views

urlpatterns = [
    path('stock/', views.stock_magasin, name='stock'),
    path('stock/centre/<int:pid>', views.stock_centre, name='stockCentre'), 
    ## url clients
    path('clients/',views.liste_clients, name='listeCl'),
    path('clients/ajouter',views.ajouter_client, name='ajouterCl'),
    path('clients/supprimer/<int:pid>/',views.supprimer_client, name='supprimerCl'),
    path('clients/modifier/<int:pid>/',views.modifier_client, name='modifierCl'),
    ## url produits
    path('produits/',views.liste_produits, name='listeP'),
    path('produits/ajouter',views.ajouter_produit, name='ajouterP'),
    path('produits/supprimer/<int:pid>/',views.supprimer_produit, name='supprimerP'),
    path('produits/modifier/<int:pid>/',views.modifier_produit, name='modifierP'),
    ## url employes
    path('employes/',views.liste_employes, name='listeE'),
    path('employes/ajouter',views.ajouter_employe, name='ajouterE'),
    path('employes/supprimer/<int:pid>/',views.supprimer_employe, name='supprimerE'),
    path('employes/modifier/<int:pid>/',views.modifier_employe, name='modifierE'),
    ## url centres
    path('centres/',views.liste_centres, name='listeCt'),
    path('centres/ajouter',views.ajouter_centre, name='ajouterCt'),
    path('centres/supprimer/<int:pid>/',views.supprimer_centre, name='supprimerCt'),
    path('centres/modifier/<int:pid>/',views.modifier_centre, name='modifierCt'),
    ## url fournisseurs
    path('fournisseurs/',views.liste_fournisseurs, name='listeF'),
    path('fournisseurs/ajouter',views.ajouter_fournisseur, name='ajouterF'),
    path('fournisseurs/supprimer/<int:pid>/',views.supprimer_fournisseur, name='supprimerF'),
    path('fournisseurs/modifier/<int:pid>/',views.modifier_fournisseur, name='modifierF'),
    ## url achats
    path('achats/',views.liste_achats, name='listeA'),
    path('achats/ajouter',views.ajouter_achat, name='ajouterA'),
    path('achats/supprimer/<int:pid>/',views.supprimer_achat, name='supprimerA'),
    path('reglement/',views.liste_reglements, name='listeReg'),
    path('reglement/paiement/<int:pid>/',views.paiement_fournisseur, name='paiementFrn'),
    ## url ventes 
    path('ventes/',views.liste_ventes, name='listeV'),
    path('ventes/ajouter',views.ajouter_vente, name='ajouterV'),
    path('ventes/supprimer/<int:pid>/',views.supprimer_vente, name='supprimerV'),
    path('credits/',views.liste_credits, name='listeCrds'),
    path('credits/paiement/<int:pid>/',views.paiement_client, name='paiementCC'),
    ## url transferts
    path('transferts/',views.liste_transferts, name='listeT'),
    path('transferts/ajouter',views.ajouter_transfert, name='ajouterT'),
    path('transferts/supprimer/<int:pid>/',views.supprimer_transfert, name='supprimerT'),
    
]