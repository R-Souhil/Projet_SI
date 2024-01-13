from django.db.models import fields
from django import forms
from .models import Centre, Produit, Employe, Client, Fournisseur


class CentreForm(forms.ModelForm):
    class Meta:
        model = Centre
        fields="__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields="__all__"
        
class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields="__all__"

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields="__all__"
        
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('prix_achat_unitaire_HT')

        if price is not None and price < 0:
            self.add_error('prix_achat_unitaire_HT', 'Le prix d\'achat ne peut pas être négatif')

        return cleaned_data

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields="__all__"