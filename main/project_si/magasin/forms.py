from django.db.models import fields
from django import forms
from .models import Centre, Produit, Employe, Client, Fournisseur, Achat, Vente, ProduitAchat, PaiementFournisseur, PaiementCreditClient


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
        fields=["nom_fournisseur","prenom_fournisseur","adresse_fournisseur","telephone_fournisseur"]
        
class PaiementCreditClientForm(forms.ModelForm):
    class Meta:
        model = PaiementCreditClient
        fields = ['date_paiement_credit_client']
        
class AchatForm(forms.ModelForm):
    class Meta:
        model = Achat
        fields = ['date_achat', 'fournisseur']
        
class PaiementFournisseurForm(forms.ModelForm):
    class Meta:
        model = PaiementFournisseur
        fields = ['date_paiement_fournisseur']
        
class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['date_vente', 'client']



        