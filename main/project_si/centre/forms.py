from django.db.models import fields
from django import forms
from .models import Centre, Produit, Employe, Client, Vente, PV, PaiementCreditClient

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields="__all__"