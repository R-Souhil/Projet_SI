from django.contrib import admin
from .models import Magasin, Fournisseur, Achat, Transfert

admin.site.register(Magasin)
admin.site.register(Fournisseur)
admin.site.register(Achat)
admin.site.register(Transfert)