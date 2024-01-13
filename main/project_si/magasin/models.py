from django.db import models

class Magasin(models.Model):
    code_magasin = models.AutoField(primary_key=True)
    nom_magasin = models.CharField(max_length=50)
    adresse_magasin = models.TextField()

    def __str__(self):
        return self.nom_magasin
    
class Centre(models.Model):
    code_centre = models.AutoField(primary_key=True)
    designation_centre = models.CharField(max_length=50)

    def __str__(self):
        return self.designation

class Produit(models.Model):
    code_produit = models.AutoField(primary_key=True)
    designation_produit = models.CharField(max_length=50)
    prix_achat_unitaire_HT = models.FloatField(max_length=30)

    def __str__(self):
        return self.designation_produit
    
class Employe(models.Model):
    code_employe = models.AutoField(primary_key=True)
    nom_employe = models.CharField(max_length=20)
    prenom_employe = models.CharField(max_length=30)
    adresse_employe = models.TextField()
    telephone_employe = models.CharField(max_length=20)
    salaire_jour = models.FloatField(max_length=30)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_employe+" "+self.prenom_employe
    
class Client(models.Model):
    code_client = models.AutoField(primary_key=True)
    nom_client = models.CharField(max_length=20)
    prenom_client = models.CharField(max_length=50)
    adresse_client = models.TextField()
    telephone_client = models.CharField(max_length=20)
    credit_client = models.FloatField(max_length=30)

    def __str__(self):
        return self.nom_client+" "+self.prenom_client
  
class Fournisseur(models.Model):
    code_fournisseur = models.AutoField(primary_key=True)
    nom_fournisseur = models.CharField(max_length=20)
    prenom_fournisseur = models.CharField(max_length=30)
    adresse_fournisseur = models.TextField()
    telephone_fournisseur = models.CharField(max_length=20)
    solde_fournisseur = models.FloatField(max_length=30)

    def __str__(self):
        return self.nom_fournisseur+" "+self.prenom_fournisseur

class Achat(models.Model):
    numero_achat = models.AutoField(primary_key=True)
    date_achat = models.DateField()
    quantite_achetee = models.IntegerField()
    montant_total_HT = models.FloatField(max_length=30)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_achat
    
class Transfert(models.Model):
    numero_transfert = models.AutoField(primary_key=True)
    date_transfert = models.DateField()
    quantite_transferee = models.IntegerField()
    cout_transfert = models.FloatField(max_length=30)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_transfert
    
class PaiementFournisseur(models.Model):
    numero_paiement_fournisseur = models.AutoField(primary_key=True)
    date_paiement_fournisseur = models.DateField()
    montant_paiement_fournisseur = models.FloatField(max_length=30)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_paiement_fournisseur
    
class AnalyseDesVentes(models.Model):
    annee = models.IntegerField()
    mois = models.IntegerField()
    taux_evolution_ventes = models.FloatField(max_length=30)
    taux_evolution_benefice = models.FloatField(max_length=30)
    top_clients = models.TextField()
    best_sellers = models.TextField()

    def str(self):
        return self.annee+"-"+self.mois
    

class AnalyseDesAchats(models.Model):
    annee = models.IntegerField
    mois = models.IntegerField
    taux_evolution_achats = models.FloatField(max_length=30)
    top_fournisseurs = models.TextField()

    def str(self):
        return self.annee+"-"+self.mois
    

    

  
class Vente(models.Model):
    numero_vente = models.AutoField(primary_key=True)
    date_vente = models.DateField()
    quantite_vendue = models.IntegerField()
    montant_total_vente = models.FloatField(max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_vente
    
class PV(models.Model):
    numero_pv = models.AutoField(primary_key=True)
    date_pv = models.DateField()
    quantite_vendue_centre = models.IntegerField()
    montant_total_vente_centre = models.FloatField(max_length=30)
    avance_salaire_employe = models.FloatField(max_length=30)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_pv
    
class PaiementCreditClient(models.Model):
    numero_paiement_credit_client = models.AutoField(primary_key=True)
    date_paiement_credit_client = models.DateField()
    montant_paiement_credit_client = models.FloatField(max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_paiement_credit_client
