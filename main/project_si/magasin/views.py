from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Magasin, Centre, Client, Produit, Employe, Vente, PV, PaiementCreditClient, Fournisseur, Achat, Transfert, PaiementFournisseur, AnalyseDesVentes, AnalyseDesAchats
from .forms import ProduitForm, ClientForm, EmployeForm, CentreForm, FournisseurForm




## Gestion Centres

def liste_centres(request):
    centres = Centre.objects.all()
    return render(request, 'centres/centres.html', {'centres': centres})

def ajouter_centre(request):
    if request.method == 'POST':
        form = CentreForm(request.POST)
        if form.is_valid():
            form.save()
            form = CentreForm()
            messages.success(request, 'Centre ajouté avec succès')
            return redirect('listeCt')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du centre. Veuillez vérifier les données.')
            return render(request, 'centres/ajouterCt.html', {"form": form})
    else:
        form = CentreForm() 
        msg = "veuillez remplir tous les informations sur votre centres"   
        return render(request,'centres/ajouterCt.html',{"form":form,"message":msg})
    
def supprimer_centre(request, pid):
    centre = get_object_or_404(Centre, code_centre=pid)
    if request.method=='POST':
        centre.delete()
        return redirect('listeCt')  
    context={'item':centre}
    return render(request,'centres/supprimerCt.html',context)
    
def modifier_centre(request, pid):
    centre = get_object_or_404(Centre, code_centre=pid)
    if request.method == 'POST':
        form = CentreForm(request.POST, instance=centre)
        if form.is_valid():
            form.save()
            return redirect('listeCt')  
    else:
        form = CentreForm(instance=centre)
    return render(request, 'centres/modifierCt.html', {'form': form, 'centre': centre})


## Gestion Clients

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/clients.html', {'clients': clients})

def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientForm()
            messages.success(request, 'Client ajouté avec succès')
            return redirect('listeCl')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du client. Veuillez vérifier les données.')
            return render(request, 'clients/ajouterCl.html', {"form": form})
    else:
        form = ClientForm() 
        msg = "veuillez remplir tous les informations sur votre client"   
        return render(request,'clients/ajouterCl.html',{"form":form,"message":msg})
    
def supprimer_client(request, pid):
    client = get_object_or_404(Client, code_client=pid)
    if request.method=='POST':
        client.delete()
        return redirect('listeCl') 
    context={'item':client}
    return render(request,'clients/supprimerCl.html',context)
    
def modifier_client(request, pid):
    client = get_object_or_404(Client, code_client=pid)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('listeCl')  
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/modifierCl.html', {'form': form, 'client': client})


## Gestion Employes

def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, 'employes/employes.html', {'employes': employes})

def ajouter_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeForm()
            messages.success(request, 'Employe ajouté avec succès')
            return redirect('listeE')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du employe. Veuillez vérifier les données.')
            return render(request, 'employes/ajouterE.html', {"form": form})
    else:
        form = EmployeForm() 
        msg = "veuillez remplir tous les informations sur votre employes"   
        return render(request,'employes/ajouterE.html',{"form":form,"message":msg})
    
def supprimer_employe(request, pid):
    employe = get_object_or_404(Employe, code_employe=pid)
    if request.method=='POST':
        employe.delete()
        return redirect('listeE')  
    context={'item':employe}
    return render(request,'employes/supprimerE.html',context)
    
def modifier_employe(request, pid):
    employe = get_object_or_404(Employe, code_employe=pid)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('listeE')  
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'employes/modifierE.html', {'form': form, 'employe': employe})


## Gestion Produits
 
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
            return render(request, 'produits/ajouterP.html', {"form": form})
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


## Gestion Fournisseurs

def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseurs/fournisseurs.html', {'fournisseurs': fournisseurs})

def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            form = FournisseurForm()
            messages.success(request, 'Fournisseur ajouté avec succès')
            return redirect('listeF')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du fournisseur. Veuillez vérifier les données.')
            return render(request, 'fournisseurs/ajouterF.html', {"form": form})
    else:
        form = FournisseurForm() 
        msg = "veuillez remplir tous les informations sur votre fournisseurs"   
        return render(request,'fournisseurs/ajouterF.html',{"form":form,"message":msg})
    
def supprimer_fournisseur(request, pid):
    fournisseur = get_object_or_404(Fournisseur, code_fournisseur=pid)
    if request.method=='POST':
        fournisseur.delete()
        return redirect('listeF')  
    context={'item':fournisseur}
    return render(request,'fournisseurs/supprimerF.html',context)
    
def modifier_fournisseur(request, pid):
    fournisseur = get_object_or_404(Fournisseur, code_fournisseur=pid)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('listeF')  
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'fournisseurs/modifierF.html', {'form': form, 'fournisseur': fournisseur})


