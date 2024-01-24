from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Magasin, Centre, Client, Produit, ProduitAchat, Employe, Vente, ProduitTransfert, StockCentre, ProduitVente, PV, StockProduit, PaiementCreditClient, Fournisseur, Achat, Transfert, PaiementFournisseur, AnalyseDesVentes, AnalyseDesAchats
from .forms import ProduitForm, ClientForm, EmployeForm, CentreForm, TransfertForm, VenteForm, PaiementCreditClientForm, FournisseurForm, AchatForm, PaiementFournisseurForm



## Gestion Centres

def liste_centres(request):
    centres = Centre.objects.all()
    return render(request, 'gestion/centres/centres.html', {'centres': centres})

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
            return render(request, 'gestion/centres/ajouterCt.html', {"form": form})
    else:
        form = CentreForm() 
        msg = "veuillez remplir tous les informations sur votre centres"   
        return render(request,'gestion/centres/ajouterCt.html',{"form":form,"message":msg})
    
def supprimer_centre(request, pid):
    centre = get_object_or_404(Centre, code_centre=pid)
    if request.method=='POST':
        centre.delete()
        return redirect('listeCt')  
    context={'item':centre}
    return render(request,'gestion/centres/supprimerCt.html',context)
    
def modifier_centre(request, pid):
    centre = get_object_or_404(Centre, code_centre=pid)
    if request.method == 'POST':
        form = CentreForm(request.POST, instance=centre)
        if form.is_valid():
            form.save()
            return redirect('listeCt')  
    else:
        form = CentreForm(instance=centre)
    return render(request, 'gestion/centres/modifierCt.html', {'form': form, 'centre': centre})

## Gestion Clients

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'gestion/clients/clients.html', {'clients': clients})

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
            return render(request, 'gestion/clients/ajouterCl.html', {"form": form})
    else:
        form = ClientForm() 
        msg = "veuillez remplir tous les informations sur votre client"   
        return render(request,'gestion/clients/ajouterCl.html',{"form":form,"message":msg})
    
def supprimer_client(request, pid):
    client = get_object_or_404(Client, code_client=pid)
    if request.method=='POST':
        client.delete()
        return redirect('listeCl') 
    context={'item':client}
    return render(request,'gestion/clients/supprimerCl.html',context)
    
def modifier_client(request, pid):
    client = get_object_or_404(Client, code_client=pid)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('listeCl')  
    else:
        form = ClientForm(instance=client)
    return render(request, 'gestion/clients/modifierCl.html', {'form': form, 'client': client})

## Gestion Employes

def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, 'gestion/employes/employes.html', {'employes': employes})

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
            return render(request, 'gestion/employes/ajouterE.html', {"form": form})
    else:
        form = EmployeForm() 
        msg = "veuillez remplir tous les informations sur votre employes"   
        return render(request,'gestion/employes/ajouterE.html',{"form":form,"message":msg})
    
def supprimer_employe(request, pid):
    employe = get_object_or_404(Employe, code_employe=pid)
    if request.method=='POST':
        employe.delete()
        return redirect('listeE')  
    context={'item':employe}
    return render(request,'gestion/employes/supprimerE.html',context)
    
def modifier_employe(request, pid):
    employe = get_object_or_404(Employe, code_employe=pid)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('listeE')  
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'gestion/employes/modifierE.html', {'form': form, 'employe': employe})

## Gestion Produits
 
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'gestion/produits/produits.html', {'produits': produits})

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
            return render(request, 'gestion/produits/ajouterP.html', {"form": form})
    else:
        form = ProduitForm() 
        msg = "veuillez remplir tous les informations sur votre produits"   
        return render(request,'gestion/produits/ajouterP.html',{"form":form,"message":msg})
    
def supprimer_produit(request, pid):
    produit = get_object_or_404(Produit, code_produit=pid)
    if request.method=='POST':
        produit.delete()
        return redirect('listeP')  
    context={'item':produit}
    return render(request,'gestion/produits/supprimerP.html',context)
    
def modifier_produit(request, pid):
    produit = get_object_or_404(Produit, code_produit=pid)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('listeP')  
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'gestion/produits/modifierP.html', {'form': form, 'produit': produit})

## Gestion Fournisseurs

def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'gestion/fournisseurs/fournisseurs.html', {'fournisseurs': fournisseurs})

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
            return render(request, 'gestion/fournisseurs/ajouterF.html', {"form": form})
    else:
        form = FournisseurForm() 
        msg = "veuillez remplir tous les informations sur votre fournisseurs"   
        return render(request,'gestion/fournisseurs/ajouterF.html',{"form":form,"message":msg})
    
def supprimer_fournisseur(request, pid):
    fournisseur = get_object_or_404(Fournisseur, code_fournisseur=pid)
    if request.method=='POST':
        fournisseur.delete()
        return redirect('listeF')  
    context={'item':fournisseur}
    return render(request,'gestion/fournisseurs/supprimerF.html',context)
    
def modifier_fournisseur(request, pid):
    fournisseur = get_object_or_404(Fournisseur, code_fournisseur=pid)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('listeF')  
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'gestion/fournisseurs/modifierF.html', {'form': form, 'fournisseur': fournisseur})

## Gestion des Achats

def liste_achats(request):
    achats=Achat.objects.all()
    montant_total_global = sum(achat.montant_total_HT for achat in achats)
    context={'achats':achats, 'montant_total_global': montant_total_global}
    return render(request,'achat/achats.html', context)

def ajouter_achat(request):
    if request.method == 'POST':
        form = AchatForm(request.POST)
        if form.is_valid():
            produits = request.POST.getlist('produits')
            if not produits:
                form.add_error(None, "Sélectionnez au moin un produit")
                return render(request, 'achat/ajouterA.html', {'form': form, 'produits': Produit.objects.all()})
            
            achat = form.save(commit=False)
            achat.save()
            for produit_id in produits:
                quantite = float(request.POST.get('quantite_' + produit_id))
                montant = Produit.objects.get(pk=produit_id).prix_achat_unitaire_HT * quantite
                prdacht = ProduitAchat(produit=Produit.objects.get(pk=produit_id), achat=achat, quantite=quantite, montant_prd=montant)
                prdacht.save()
                try:
                    stock = StockProduit.objects.get(produit=Produit.objects.get(pk=produit_id))
                except StockProduit.DoesNotExist:
                    stock = StockProduit.objects.create(produit=Produit.objects.get(pk=produit_id), stock=Magasin.objects.get(code_magasin=1))
                stock.qteDispo += quantite
                stock.save()    
                
            montantT = float(request.POST.get('montantT'))
            sompay = float(request.POST.get('sommepaye'))
            frn = achat.fournisseur
            pfrn = PaiementFournisseur(
                date_paiement_fournisseur=achat.date_achat, montant_paiement_fournisseur=sompay, fournisseur=achat.fournisseur
                )
            pfrn.save()
            # le cas du paymenet partiel
            if sompay < montantT:
                frn.solde_fournisseur += montantT - sompay
                frn.save()
                
            achat.montant_total_HT = montantT
            achat.montant_paye = sompay
            achat.save()
            return redirect('listeA')
    else:
        form = AchatForm()
    return render(request, 'achat/ajouterA.html', {'form': form, 'produits': Produit.objects.all()})    
    
def supprimer_achat(request, pid):
    achat = get_object_or_404(Achat, numero_achat=pid)
    if request.method=='POST':
        # annulez le solde ajouté precedemment et supprimer le paiement et diminuer le stock
        pays = PaiementFournisseur.objects.get(fournisseur=achat.fournisseur, date_paiement_fournisseur=achat.date_achat, montant_paiement_fournisseur=achat.montant_paye)
        if achat.montant_total_HT > achat.montant_paye:
            frn = achat.fournisseur
            frn.solde_fournisseur -= achat.montant_total_HT - achat.montant_paye
            frn.save()
            pays.delete()
            
        prds = ProduitAchat.objects.filter(achat=achat)
        for prd in prds:
            prdstock = StockProduit.objects.get(produit=prd.produit)
            prdstock.qteDispo -= prd.quantite
            if prdstock.qteDispo == 0:
                prdstock.delete()
            else:
                prdstock.save()
            prd.delete()
        achat.delete()
        return redirect('listeA')  
    context={'item':achat, 'produits': ProduitAchat.objects.filter(achat=achat)}
    return render(request,'achat/supprimerA.html',context)

def liste_reglements(request):
    frns = Fournisseur.objects.all()
    pays = PaiementFournisseur.objects.all()
    return render(request, 'achat/reglements.html', {'fournisseurs': frns, 'pays': pays})

def paiement_fournisseur(request,pid):
    frn = Fournisseur.objects.get(pk=pid)
    if request.method == 'POST':
        form = PaiementFournisseurForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date_paiement_fournisseur']
            montant = float(request.POST.get('montant_paye'))
            
            pfrn = PaiementFournisseur(
                date_paiement_fournisseur=date,
                montant_paiement_fournisseur=montant,
                fournisseur=frn
            )
            pfrn.save()
            
            frn.solde_fournisseur -= montant
            frn.save()
            return redirect('listeReg')
    else:
        form = PaiementFournisseurForm()
    return render(request, 'achat/paiementF.html', {'form': form, 'f': frn})

def stock_magasin(request):
    try:
        s=Magasin.objects.get(code_magasin='1')
    except:
        s=Magasin.objects.create(code_magasin='1',nom_magasin='Magasin Principal')
    valeurTotal = sum(stock.produit.prix_achat_unitaire_HT * stock.qteDispo for stock in StockProduit.objects.all())
    s.valeur_stock = valeurTotal
    s.save()
    sp=StockProduit.objects.all()
    context={'sp':sp, 'v':valeurTotal}
    return render(request, 'stock.html', context)

def stock_centre(request,pid):
    try:
        c=Centre.objects.get(code_centre=pid)
    except:
        c=Centre.objects.create(code_centre=pid,nom_magasin='Centre'+pid)
    valeurTotal = sum(stock.produit.prix_achat_unitaire_HT * stock.qteDispo for stock in StockCentre.objects.filter(stock=c))
    sc = StockCentre.objects.filter(stock=c)
    context={'sc':sc,'c':c, 'v':valeurTotal}
    return render(request, 'stockCtr.html', context)

## Gestion Ventes

def liste_ventes(request):
    ventes=Vente.objects.all()
    montant_total_global = sum(vente.montant_total_vente for vente in ventes)
    benefice_total = sum(vente.benefice_vente for vente in ventes)
    context={'ventes':ventes, 'montant_total_global': montant_total_global, 'benefice': benefice_total}
    return render(request,'vente/ventes.html', context)

def ajouter_vente(request):
    montantTachat = 0
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            produits = request.POST.getlist('produits')
            if not produits:
                form.add_error(None, "Sélectionnez au moin un produit")
                return render(request, 'vente/ajouterV.html', {'form': form, 'stock': StockProduit.objects.all()})
            
            vente = form.save(commit=False)
            vente.save()
            for produit_id in produits:
                quantite = float(request.POST.get('quantite_' + produit_id))
                prixVente = float(request.POST.get('prix_' + produit_id))
                montant = prixVente * quantite
                prdvente = ProduitVente(
                    produit=Produit.objects.get(pk=produit_id),
                    vente=vente,
                    quantite=quantite,
                    montant_vente_prd=montant,
                    prix_vente_unite=prixVente
                    )
                prdvente.save()
                stock = StockProduit.objects.get(produit=Produit.objects.get(pk=produit_id))
                stock.qteDispo -= quantite
                if stock.qteDispo == 0:
                    stock.delete()
                else:
                    stock.save()
                montantTachat += Produit.objects.get(pk=produit_id).prix_achat_unitaire_HT * quantite
                
            montantT = float(request.POST.get('montantT'))
            somrecue = float(request.POST.get('sommerecue'))
            cl = vente.client
            pccl = PaiementCreditClient(
                date_paiement_credit_client=vente.date_vente, montant_paiement_credit_client=somrecue, client=cl
                )
            pccl.save()
            # le cas du paiemenet partiel on ajoute le montant restant au credit du client
            if somrecue < montantT:
                cl.credit_client += montantT - somrecue
                cl.save()    
            
            vente.benefice_vente = montantT - montantTachat
            vente.montant_total_vente = montantT
            vente.montant_recue = somrecue
            vente.save()
            return redirect('listeV')
    else:
        form = VenteForm()
        return render(request, 'vente/ajouterV.html', {'form': form, 'stock': StockProduit.objects.all()}) 
    
def supprimer_vente(request, pid):
    vente = get_object_or_404(Vente, numero_vente=pid)
    if request.method=='POST':
        # annulez le crédit ajouté precedemment et supprimer le paiement et remplir le stock
        pays = PaiementCreditClient.objects.get(client=vente.client, date_paiement_credit_client=vente.date_vente, montant_paiement_credit_client=vente.montant_recue)
        if vente.montant_total_vente > vente.montant_recue:
            client = vente.client
            client.credit_client -= vente.montant_total_vente - vente.montant_recue
            client.save()
            pays.delete()
            
        vprds = ProduitVente.objects.filter(vente=vente)
        for vprd in vprds:
            try:
                prdstock = StockProduit.objects.get(produit=vprd.produit)
                prdstock.qteDispo += vprd.quantite
                prdstock.save()
            except StockProduit.DoesNotExist:
                StockProduit.objects.create(
                    produit=vprd.produit,
                    stock=Magasin.objects.get(code_magasin=1),
                    qteDispo=vprd.quantite
                )
                prdstock.save()
            
            vprd.delete()
        vente.delete()
        return redirect('listeV')  
    context={'item':vente, 'produits': ProduitVente.objects.filter(vente=vente)}
    return render(request,'vente/supprimerV.html',context)

def liste_credits(request):
    cls = Client.objects.all()
    pays = PaiementCreditClient.objects.all()
    return render(request, 'vente/credits.html', {'clients': cls, 'pays': pays})

def paiement_client(request,pid):
    cl = Client.objects.get(pk=pid)
    if request.method == 'POST':
        form = PaiementCreditClientForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date_paiement_credit_client']
            montant = float(request.POST.get('montant_paye'))
            
            pcl = PaiementCreditClient(
                date_paiement_credit_client=date,
                montant_paiement_credit_client=montant,
                client=cl
            )
            pcl.save()
            
            cl.credit_client -= montant
            cl.save()
            return redirect('listeCrds')
    else:
        form = PaiementCreditClientForm()
    return render(request, 'vente/paiementClient.html', {'form': form, 'c': cl})

## Gestion Transferts

def liste_transferts(request):
    transferts=Transfert.objects.all()
    context={'ts':transferts}
    return render(request,'transfert/transferts.html', context)

def ajouter_transfert(request):
    montant_Transfert = 0
    if request.method == 'POST':
        form = TransfertForm(request.POST)
        if form.is_valid():
            produits = request.POST.getlist('produits')
            if not produits:
                form.add_error(None, "Sélectionnez au moin un produit")
                return render(request, 'transfert/ajouterT.html', {'form': form, 'stock': StockProduit.objects.all()})
            transfert = form.save(commit=False)
            transfert.save()
            for p in produits:
                quantite = float(request.POST.get('quantite_' + p))
                montant = Produit.objects.get(pk=p).prix_achat_unitaire_HT * quantite
                montant_Transfert += montant * quantite
                prdtrns = ProduitTransfert(
                    produit=Produit.objects.get(pk=p),
                    transfert=transfert,
                    quantite=quantite
                    )
                prdtrns.save()
                stock = StockProduit.objects.get(produit=Produit.objects.get(pk=p))
                stock.qteDispo -= quantite
                if stock.qteDispo == 0:
                    stock.delete()
                else:
                    stock.save()
                try:
                    stockCentre = StockCentre.objects.get(stock=transfert.centre, produit=Produit.objects.get(pk=p))
                    stockCentre.qteDispo += quantite
                    stockCentre.save()
                except StockCentre.DoesNotExist:
                    stockCentre = StockCentre(
                        stock=transfert.centre,
                        produit=Produit.objects.get(pk=p),
                        qteDispo = quantite
                    )
                    stockCentre.save()
            transfert.cout_transfert = montant_Transfert
            transfert.save()
            return redirect('listeT')
    else:
        form = TransfertForm()  
        return render(request, 'transfert/ajouterT.html', {'form': form, 'stock': StockProduit.objects.all()})

def supprimer_transfert(request, pid):
    transfert = get_object_or_404(Transfert, numero_transfert=pid)
    if request.method=='POST':
        # supprimer le transferet diminuer le stock du centre et remplir le stock du magasin
        tprds = ProduitTransfert.objects.filter(transfert=transfert)
        for tprd in tprds:
            try:
                prdstock = StockProduit.objects.get(produit=tprd.produit)
                prdstock.qteDispo += tprd.quantite
                prdstock.save()
            except StockProduit.DoesNotExist:
                StockProduit.objects.create(
                    produit=tprd.produit,
                    stock=Magasin.object.get(code_magasin=1),
                    qteDispo=tprd.quantite
                )
                prdstock.save()
                
            prdstockCtr = StockCentre.objects.get(stock=transfert.centre,produit=tprd.produit)
            prdstockCtr.qteDispo -= tprd.quantite
            if prdstock.qteDispo <= 0:
                prdstockCtr.delete()
            else:
                prdstockCtr.save()
            tprd.delete()
        transfert.delete()
        return redirect('listeT')  
    else:
        context={'item':transfert, 'produits': ProduitTransfert.objects.filter(transfert=transfert)}
        return render(request,'transfert/supprimerT.html',context)


