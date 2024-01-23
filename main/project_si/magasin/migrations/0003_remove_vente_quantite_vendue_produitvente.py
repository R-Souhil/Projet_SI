# Generated by Django 5.0 on 2024-01-23 17:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0002_vente_montant_recue_alter_client_adresse_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vente',
            name='quantite_vendue',
        ),
        migrations.CreateModel(
            name='ProduitVente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('montant_vente_prd', models.FloatField()),
                ('prix_vente_unite', models.FloatField()),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.produit')),
                ('vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.vente')),
            ],
        ),
    ]
