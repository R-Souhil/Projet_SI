from django.contrib import admin
from .models import Centre, Client, Produit, Employe, Vente, PV, PaiementCreditClient

admin.site.register(Centre)
admin.site.register(Client)
admin.site.register(Produit)
admin.site.register(Employe)
admin.site.register(Vente)
admin.site.register(PV)
admin.site.register(PaiementCreditClient)
