from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Centre, Produit, Employe, Client, Vente, PV, PaiementCreditClient
from .forms import ProduitForm
 
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/produits.html', {'produits': produits})

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProduitForm()
            messages.success(request, 'Produit ajouté avec succès')
            return redirect('listeP')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du produit. Veuillez vérifier les données.')
    else:
        form = ProduitForm() 
        msg = "veuillez remplir tous les informations sur votre produits"   
        return render(request,'produits/ajouterP.html',{"form":form,"message":msg})
    
def supprimer_produit(request, pid):
    produit = get_object_or_404(Produit, code_produit=pid)
    if request.method=='POST':
        produit.delete()
        return redirect('listeP')  
    context={'item':produit}
    return render(request,'produits/supprimerP.html',context)
    
def modifier_produit(request, pid):
    produit = get_object_or_404(Produit, code_produit=pid)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('listeP')  
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produits/modifierP.html', {'form': form, 'produit': produit})

def centre1(request, cid):
    centre = get_object_or_404(Centre, code_centre=cid)
    return render(request, 'centre.html', {'centre': centre})
