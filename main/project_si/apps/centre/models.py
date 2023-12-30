from django.db import models

class Centre(models.Model):
    code_centre = models.AutoField(primary_key=True)
    désignation = models.CharField(max_length=50)

    def __str__(self):
        return f"Centre {self.désignation}"
    
class Produit(models.Model):
    code_produit = models.AutoField(primary_key=True)
    designation_produit = models.CharField(max_length=50)
    prix_achat_unitaire_HT = models.FloatField(max_length=30)

    def __str__(self):
        return f"Produit: {self.designation_produit}"
    
class Employe(models.Model):
    code_employe = models.AutoField(primary_key=True)
    nom_employe = models.CharField(max_length=20)
    prenom_employe = models.CharField(max_length=30)
    adresse_employe = models.TextField()
    telephone_employe = models.CharField(max_length=20)
    salaire_jour = models.DecimalField(max_length=30)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employé: {self.nom_employe} {self.prenom_employe}"
    
class Client(models.Model):
    code_client = models.AutoField(primary_key=True)
    nom_client = models.CharField(max_length=20)
    prenom_client = models.CharField(max_length=50)
    adresse_client = models.TextField()
    telephone_client = models.CharField(max_length=20)
    credit_client = models.FloatField(max_length=30)

    def __str__(self):
        return f"Client: {self.nom_client} {self.prenom_client}"
  
class Vente(models.Model):
    numero_vente = models.AutoField(primary_key=True)
    date_vente = models.DateField()
    quantite_vendue = models.IntegerField()
    montant_total_vente = models.FloatField(max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vente {self.numero_vente}"
    
class PV(models.Model):
    numero_pv = models.AutoField(primary_key=True)
    date_pv = models.DateField()
    quantite_vendue_centre = models.IntegerField()
    montant_total_vente_centre = models.FloatField(max_length=30)
    avance_salaire_employe = models.FloatField(max_length=30)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)

    def __str__(self):
        return f"PV {self.numero_pv}"