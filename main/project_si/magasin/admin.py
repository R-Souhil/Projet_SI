from django.contrib import admin
from .models import Magasin, Centre, Client, Produit, ProduitAchat, Employe, Vente, PV, PaiementCreditClient, Fournisseur, Achat, Transfert, PaiementFournisseur, AnalyseDesVentes, AnalyseDesAchats

admin.site.register(Magasin)
admin.site.register(Fournisseur)
admin.site.register(Centre)
admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Employe)
admin.site.register(Vente)
admin.site.register(Achat)
admin.site.register(ProduitAchat)
admin.site.register(Transfert)
admin.site.register(PaiementFournisseur)
admin.site.register(AnalyseDesVentes)
admin.site.register(AnalyseDesAchats)
admin.site.register(PV)
admin.site.register(PaiementCreditClient)