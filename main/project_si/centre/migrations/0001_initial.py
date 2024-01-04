# Generated by Django 5.0 on 2024-01-04 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('code_centre', models.AutoField(primary_key=True, serialize=False)),
                ('désignation', models.CharField(max_length=50)),
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
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.centre')),
            ],
        ),
        migrations.CreateModel(
            name='PaiementCreditClient',
            fields=[
                ('numero_paiement_credit_client', models.AutoField(primary_key=True, serialize=False)),
                ('date_paiement_credit_client', models.DateField()),
                ('montant_paiement_credit_client', models.FloatField(max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.client')),
            ],
        ),
        migrations.CreateModel(
            name='PV',
            fields=[
                ('numero_pv', models.AutoField(primary_key=True, serialize=False)),
                ('date_pv', models.DateField()),
                ('quantite_vendue_centre', models.IntegerField()),
                ('montant_total_vente_centre', models.FloatField(max_length=30)),
                ('avance_salaire_employe', models.FloatField(max_length=30)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.centre')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('numero_vente', models.AutoField(primary_key=True, serialize=False)),
                ('date_vente', models.DateField()),
                ('quantite_vendue', models.IntegerField()),
                ('montant_total_vente', models.FloatField(max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.client')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.produit')),
            ],
        ),
    ]
