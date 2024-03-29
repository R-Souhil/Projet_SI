# Generated by Django 5.0 on 2024-01-23 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0005_vente_benefice_vente'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockCentre',
            fields=[
                ('primary_key', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('qteDispo', models.PositiveIntegerField(default=0)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.produit')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.centre')),
            ],
        ),
    ]
