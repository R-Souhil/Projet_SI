from django.contrib import admin
from .models import Magasin, Fournisseur, Achat, Transfert, PaiementFournisseur, AnalyseDesVentes, AnalyseDesAchats

admin.site.register(Magasin)
admin.site.register(Fournisseur)
admin.site.register(Achat)
admin.site.register(Transfert)
admin.site.register(PaiementFournisseur)
admin.site.register(AnalyseDesVentes)
admin.site.register(AnalyseDesAchats)