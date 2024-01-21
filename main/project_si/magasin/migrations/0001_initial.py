# Generated by Django 5.0 on 2024-01-21 20:37

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyseDesAchats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taux_evolution_achats', models.FloatField(max_length=30)),
                ('top_fournisseurs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AnalyseDesVentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.IntegerField()),
                ('mois', models.IntegerField()),
                ('taux_evolution_ventes', models.FloatField(max_length=30)),
                ('taux_evolution_benefice', models.FloatField(max_length=30)),
                ('top_clients', models.TextField()),
                ('best_sellers', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('code_centre', models.AutoField(primary_key=True, serialize=False)),
                ('designation_centre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('code_client', models.AutoField(primary_key=True, serialize=False)),
                ('nom_client', models.CharField(max_length=20)),
                ('prenom_client', models.CharField(max_length=50)),
                ('adresse_client', models.TextField()),
                ('telephone_client', models.CharField(max_length=20)),
                ('credit_client', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('code_fournisseur', models.AutoField(primary_key=True, serialize=False)),
                ('nom_fournisseur', models.CharField(max_length=20)),
                ('prenom_fournisseur', models.CharField(max_length=30)),
                ('adresse_fournisseur', models.CharField(max_length=100)),
                ('telephone_fournisseur', models.CharField(max_length=20)),
                ('solde_fournisseur', models.FloatField(default=0, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Magasin',
            fields=[
                ('code_magasin', models.AutoField(primary_key=True, serialize=False)),
                ('nom_magasin', models.CharField(max_length=50)),
                ('adresse_magasin', models.TextField()),
                ('valeur_stock', models.FloatField(default=0, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('code_produit', models.AutoField(primary_key=True, serialize=False)),
                ('designation_produit', models.CharField(max_length=50)),
                ('prix_achat_unitaire_HT', models.FloatField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('code_employe', models.AutoField(primary_key=True, serialize=False)),
                ('nom_employe', models.CharField(max_length=20)),
                ('prenom_employe', models.CharField(max_length=30)),
                ('adresse_employe', models.TextField()),
                ('telephone_employe', models.CharField(max_length=20)),
                ('salaire_jour', models.FloatField(max_length=30)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.centre')),
            ],
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('numero_achat', models.AutoField(primary_key=True, serialize=False)),
                ('date_achat', models.DateField(default=django.utils.timezone.now)),
                ('montant_total_HT', models.FloatField(default=0)),
                ('montant_paye', models.FloatField(default=0)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='PaiementCreditClient',
            fields=[
                ('numero_paiement_credit_client', models.AutoField(primary_key=True, serialize=False)),
                ('date_paiement_credit_client', models.DateField(default=django.utils.timezone.now)),
                ('montant_paiement_credit_client', models.FloatField(max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.client')),
            ],
        ),
        migrations.CreateModel(
            name='PaiementFournisseur',
            fields=[
                ('numero_paiement_fournisseur', models.AutoField(primary_key=True, serialize=False)),
                ('date_paiement_fournisseur', models.DateField(default=django.utils.timezone.now)),
                ('montant_paiement_fournisseur', models.FloatField(max_length=30)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitAchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('montant_prd', models.FloatField()),
                ('achat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.achat')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.produit')),
            ],
        ),
        migrations.CreateModel(
            name='PV',
            fields=[
                ('numero_pv', models.AutoField(primary_key=True, serialize=False)),
                ('date_pv', models.DateField(default=django.utils.timezone.now)),
                ('quantite_vendue_centre', models.IntegerField()),
                ('montant_total_vente_centre', models.FloatField(max_length=30)),
                ('avance_salaire_employe', models.FloatField(max_length=30)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.centre')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.employe')),
            ],
        ),
        migrations.CreateModel(
            name='StockProduit',
            fields=[
                ('primary_key', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('qteDispo', models.PositiveIntegerField(default=0)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.produit')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.magasin')),
            ],
        ),
        migrations.CreateModel(
            name='Transfert',
            fields=[
                ('numero_transfert', models.AutoField(primary_key=True, serialize=False)),
                ('date_transfert', models.DateField(default=django.utils.timezone.now)),
                ('quantite_transferee', models.IntegerField()),
                ('cout_transfert', models.FloatField(max_length=30)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.centre')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('numero_vente', models.AutoField(primary_key=True, serialize=False)),
                ('date_vente', models.DateField(default=django.utils.timezone.now)),
                ('quantite_vendue', models.IntegerField()),
                ('montant_total_vente', models.FloatField(max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.client')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.produit')),
            ],
        ),
    ]
