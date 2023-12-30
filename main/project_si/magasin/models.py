from django.db import models
from centre.models import Produit, Centre, Client

class Magasin(models.Model):
    code_magasin = models.AutoField(primary_key=True)
    nom_magasin = models.CharField(max_length=50)
    adresse_magasin = models.TextField()

    def __str__(self):
        return f"Magasin: {self.nom_magasin}"
  
class Fournisseur(models.Model):
    code_fournisseur = models.AutoField(primary_key=True)
    nom_fournisseur = models.CharField(max_length=20)
    prenom_fournisseur = models.CharField(max_length=30)
    adresse_fournisseur = models.TextField()
    telephone_fournisseur = models.CharField(max_length=20)
    solde_fournisseur = models.FloatField(max_length=30)

    def __str__(self):
        return f"Fournisseur: {self.nom_fournisseur} {self.prenom_fournisseur}"

class Achat(models.Model):
    numero_achat = models.AutoField(primary_key=True)
    date_achat = models.DateField()
    quantite_achetee = models.IntegerField()
    montant_total_HT = models.FloatField(max_length=30)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Achat {self.numero_achat}"
    
class Transfert(models.Model):
    numero_transfert = models.AutoField(primary_key=True)
    date_transfert = models.DateField()
    quantite_transferee = models.IntegerField()
    cout_transfert = models.FloatField(max_length=30)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transfert {self.numero_transfert}"
    
class PaiementFournisseur(models.Model):
    numero_paiement_fournisseur = models.AutoField(primary_key=True)
    date_paiement_fournisseur = models.DateField()
    montant_paiement_fournisseur = models.FloatField(max_length=30)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return f"Paiement Fournisseur {self.numero_paiement_fournisseur}"
    
class AnalyseDesVentes(models.Model):
    annee = models.IntegerField()
    mois = models.IntegerField()
    taux_evolution_ventes = models.FloatField(max_length=30)
    taux_evolution_benefice = models.FloatField(max_length=30)
    top_clients = models.TextField()
    best_sellers = models.TextField()

    def str(self):
        return f"Analyse des Ventes {self.annee} - {self.mois}"
    