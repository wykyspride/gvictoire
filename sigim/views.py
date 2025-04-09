from django.http import JsonResponse ,HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db.models import Q
from .models import regfactm,modereglement,facture,personnel,prestations,newuser,typepiece,proprietaire,bien,compbien,status,client,contrat,tests,proforma,detailsfacture,detailsproforma,mandat
import os, os.path
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, date
from django.contrib.auth import authenticate, login, logout
from .form import composantsForm, biensForm, formtest
from django.template.loader import get_template
import pdfkit
from num2words import num2words
from django.views.generic import View
from xhtml2pdf import pisa


#Espace test
def maquette(request):
    return render(request,'maquette.html')




# Accueil.
def home(request):
    return render(request,'index.html')


# Espace Staff
def espacestaff(request):
    return render(request,'staffpage.html')




# Connexion.
def conex(request):
    if request.method == "POST":
        email = request.POST.get('admail', None)
        password = request.POST.get('password', None)
        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
             #Si le mail et le mot de passe sont justes, il se connecte
            if auth_user:
                login(request, auth_user)

                #Notification de derniere connextion
                #notif=send_mail('Notification de connexion','Nous vous envoyons ce message parceque nous avons constaté une connexion sur votre espace client djafa à la date du:'+' '+str(datetime.today())+"\n"+"\n"+ 'Cordialement','kobenanwykys@gmail.com',[email],fail_silently=False)
                
                #Redirection vers la page superadmin selon qu'il soit designé comme superadmin
                if user.is_authenticated and user.is_superuser:
                    return redirect('espaceadmin')
                
                #Redirection vers la page staff selon qu'il soit designé comme un memebre du staff
                if user.is_authenticated and user.is_staff:
                    return redirect('espacestaff')
                
                #Sinon Redirection vers la page d'accueil
                else:
                    return redirect('home')

            else:
                print("mot de passe incorrecte")
        else:
            print("L'utilisateur n'existe pas")
    return render(request, 'conex.html', {})
    



# Creation des utilisateurs
def aduser(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('nom', None)
        email = request.POST.get('admail', None)
        first_name = request.POST.get('nom', None)
        last_name = request.POST.get('contact', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)

#ENREGISTREMENT DANS LE FICHIER CLIENT
        nom=request.POST.get('nom')
        contact=request.POST.get('contact')
        admail=request.POST.get('admail')
        localisation=request.POST.get('localisation')
        genre=request.POST.get('genre')
        photoid=request.POST.get('photoid')
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Entrer un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mots de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        # register
        if error == False:
            user = User(username = name, email = email,first_name=first_name,last_name=last_name)
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()

        #Enregistrement client
            user_id=user.id

            savenewuser=newuser.objects.create(user_id=user_id,nom=nom,contact=contact,admail=admail,localisation=localisation,genre=genre,photoid=photoid)
            savenewuser.save()
        #Notification par mail du compte crée
            #notif=send_mail('Création de compte','Nous vous envoyons ce message parceque votre compte a bien été crée dans notre système.'+' '+str(datetime.today())+"\n"+'Lien de connexion:'+' '+'www.djafa.pythonanywhere/conex'+"\n"+"\n"+ 'Cordialement','kobenanwykys@gmail.com',[email],fail_silently=False)
            return redirect('conex')

    context = {'error':error,'message':message}
    return render(request, 'aduser.html', context)

#Espace personnel/USERS
def espacepersonnel(request):
    lesusers=newuser.objects.all()
    context={'lesusers':lesusers}
    return render (request,'espacepersonnel.html', context)

#Ajout type piece
def adypepiece(request):
    if request.method =="POST":
        libelle=request.POST.get('nom')
        savetypepiece=typepiece.objects.create(libelle=libelle)
        savetypepiece.save()
    return render(request,'typepiece.html')




#Ajout Proprietaiire
def adproprio(request):
    if request.method =='POST':
        nom=request.POST.get('nom')
        fonctions=request.POST.get('fonctions')
        numpiece=request.POST.get('numpiece')
        contact1=request.POST.get('contact1')
        contact2=request.POST.get('contact2')
        lieuhabitation=request.POST.get('lieuhabitation')
        photo=request.POST.get('photo')
        adressemail=request.POST.get('adressemail')
        naturepiece=request.POST.get('naturepiece')
        datevalidepiece=request.POST.get('datevalidepiece')
        situationmatrimoniale=request.POST.get('situationmatrimoniale')
        personneurgence=request.POST.get('personneurgence')
        contacturgence=request.POST.get('contacturgence')
        lieunaissance=request.POST.get('lieunaissance')
        statut='Attente'
        nationnalite=request.POST.get('nationnalite')
        representant=request.POST.get('representant')
        contact1representant=request.POST.get('contact1representant')
        numcompte=request.POST.get('numcompte')
        datenais=request.POST.get('datenais')
        boitepostale=request.POST.get('boitepostale')

        saveproprio=proprietaire.objects.create(statut=statut,nom=nom,fonctions=fonctions,numpiece=numpiece,contact1=contact1,contact2=contact2, lieuhabitation=lieuhabitation,photo=photo,adressemail=adressemail, naturepiece=naturepiece,datevalidepiece=datevalidepiece,situationmatrimoniale=situationmatrimoniale,personneurgence=personneurgence,contacturgence=contacturgence,datenais=datenais,lieunaissance=lieunaissance,nationnalite=nationnalite,representant=representant,contact1representant=contact1representant,numcompte=numcompte,boitepostale=boitepostale)
        saveproprio.save()
    return render(request,'adproprio.html')



#Modif Proprietaiire
def modifproprio(request, id):
    leproprio=proprietaire.objects.get(id=id)
    listestatus=status.objects.all()
    context={'leproprio':leproprio, 'listestatus':listestatus}
    if request.method =='POST':
        leproprio.nom=request.POST.get('nom')
        leproprio.fonctions=request.POST.get('fonctions')
        leproprio.numpiece=request.POST.get('numpiece')
        leproprio.contact1=request.POST.get('contact1')
        leproprio.contact2=request.POST.get('contact2')
        leproprio.lieuhabitation=request.POST.get('lieuhabitation')
        leproprio.photo=request.POST.get('photo')
        leproprio.adressemail=request.POST.get('adressemail')
        leproprio.naturepiece=request.POST.get('naturepiece')
        leproprio.datevalidepiece=request.POST.get('datevalidepiece')
        leproprio.situationmatrimoniale=request.POST.get('situationmatrimoniale')
        leproprio.personneurgence=request.POST.get('personneurgence')
        leproprio.contacturgence=request.POST.get('contacturgence')
        leproprio.lieunaissance=request.POST.get('lieunaissance')
        leproprio.statut=request.POST.get('statut')
        leproprio.nationnalite=request.POST.get('nationnalite')
        leproprio.representant=request.POST.get('representant')
        leproprio.contact1representant=request.POST.get('contact1representant')
        leproprio.numcompte=request.POST.get('numcompte')
        leproprio.datenais=request.POST.get('datenais')
        leproprio.boitepostale=request.POST.get('boitepostale')

        leproprio.save()
        return redirect (espaceproprio)
    return render(request,'modifproprio.html', context)

#Prospect proprio
def propsectproprio(request):
    listeproprio=proprietaire.objects.filter(statut='Attente')
    context={'listeproprio':listeproprio}
    return render (request,'propsectproprio.html',context)


#PROFORMA MANDAT
def proformamandat(request):
    lesproformas=proforma.objects.filter(typeproforma='mandat')
    context={'lesproformas':lesproformas}
    return render (request, 'proformamandat.html',context)



#AJOUT PROFORMA  MANDAT 
def adprofmanda(request,id):
    lesbiens=bien.objects.all()
    lespres=prestations.objects.all()
    leproprio=proprietaire.objects.get(id=id)
    context={'leproprio':leproprio, 'lesbiens':lesbiens,'lespres':lespres}
    if request.method=="POST":
        client_id= request.POST.get("client")
        numquitance=  request.POST.get("numquitance")
        delaispaiement=  request.POST.get("delaispaiement")
        bien_id=request.POST.get("bien")
        typebail= request.POST.get("typebail")
        commercial_id=request.POST.get("commercial")
        soustotal= request.POST.get("soustotal")
        totaltva=request.POST.get("totaltva")
        totalttc=request.POST.get("totalttc")
        remise=request.POST.get("remise")
        netapayer=request.POST.get("netapayer")

        #saveproforma=proforma.objects.create(client_id=client_id,numquitance=numquitance,delaispaiement=delaispaiement,bien_id=bien_id,typebail=typebail,commercial_id=commercial_id,soustotal=soustotal,totaltva=totaltva,totalttc=totalttc,remise=remise,netapayer=netapayer)
        #saveproforma.save()

        #ENREGISTREMENT DES DETAILS
        proforma_id= []
        description= [request.POST.get("t_description")]
        soustotal= []
        totaltva= []
        totalttc= []
        remise= []
        netapayer= []
        print (description)
    return render (request, 'adprofmanda.html',context)



#PROFORMA  BAIL CLIENT
def proformabail(request):
    lesproformas=proforma.objects.filter(typeproforma='bail')
    context={'lesproformas':lesproformas}
    return render (request, 'proformabail.html',context)


#AJOUT PROFORMA  BAIL CLIENT
def adproformabail(request, id):
    leclient=client.objects.get(id=id)
    context={'leclient':leclient}
    return render (request, 'adproformbail.html', context)



#PROSPECT CONTRATS PROPRIO
def prospectcontratrpo (request):
    lescontrats=contrat.objects.filter(statut='Attente')
    context={'lescontrats':lescontrats}
    return render (request, 'prospectcontrat.html',context)


#Espace proprietaire
def espaceproprio(request):
    listeproprio=proprietaire.objects.filter(statut='valide')
    context={'listeproprio':listeproprio}
    return render(request, 'espaceproprio.html',context)


#Espace ajout des biens
def adbien(request):
    listeproprio=proprietaire.objects.all()
    context={'listeproprio':listeproprio}
    if request.method=='POST':
        #origine=os.path(request.POST.get('docs'))
        #destination="c:/gvictoire/"+str(request.POST.get('docs'))
        #os.replace(origine,destination)

        nom=request.POST.get('nom')
        localisation=request.POST.get('localisation')
        commentaire=request.POST.get('commentaire')
        lot=request.POST.get('lot')
        iLot=request.POST.get('ilot')
        superficie=request.POST.get('superficie')
        legislationbau=request.POST.get('legislationbau')
        delaispaiement=request.POST.get('delaispaiement')
        status="Attente"
        circonscription=request.POST.get('circonscription')
        revenumensuel=request.POST.get('revenumensuel')
        usage=request.POST.get('usage')
        commune=request.POST.get('commune')
        quartier=request.POST.get('quartier')
        proprietaire_id=request.POST.get('proprietaire')
        typebien=request.POST.get('typebien')
        caution=request.POST.get('caution')
        loyeravance=request.POST.get('loyeravance')
        cautioncie=request.POST.get('cautioncie')
        fraisagence=request.POST.get('fraisagence')
        enregistrementbail=request.POST.get('enregistrementbail')
        assurance=request.POST.get('assurance')
        fraisrenouvellement=request.POST.get('fraisrenouvellement')
        docs=request.POST.get('docs')
        savebien=bien.objects.create(nom=nom,localisation=localisation,commentaire=commentaire,lot=lot,iLot=iLot,superficie=superficie,legislationbau=legislationbau,delaispaiement=delaispaiement,status=status,circonscription=circonscription,revenumensuel=revenumensuel,usage=usage,commune=commune,quartier=quartier,proprietaire_id=proprietaire_id,typebien=typebien,caution=caution ,cautioncie=cautioncie ,fraisagence=fraisagence ,enregistrementbail=enregistrementbail ,assurance=assurance,fraisrenouvellement=fraisrenouvellement,docs=docs,loyeravance=loyeravance)
        savebien.save()
        return redirect ('prospectbien')
    return render(request,'adbien.html',context)



#PROSPECT BIEN
def prospectbien(request):
    listeprospect=bien.objects.filter(status='Attente')
    context={'listeprospect':listeprospect}
    return render(request,'prospectbien.html',context)

#Modif Bien
def modifbien(request,id):
    lebien=bien.objects.get(id=id)
    listeproprio=proprietaire.objects.all()
    listestatus=status.objects.all()
    context={'lebien':lebien,'listeproprio':listeproprio,'listestatus':listestatus}
    if request.method=='POST':
        #olddestination="C:/gvictoire/images/documents/"+str(lebien.docs)
        #newdestination="c:/gvictoire/"+str(request.POST.get('docs'))
        #os.replace(olddestination,newdestination)
        lebien.status=request.POST.get("statut")
        lebien.nom=request.POST.get('nom')
        lebien.datecreation=lebien.datecreation
        lebien.localisation=request.POST.get('localisation')
        lebien.commentaire=request.POST.get('commentaire')
        lebien.lot=request.POST.get('lot')
        lebien.iLot=request.POST.get('ilot')
        lebien.superficie=request.POST.get('superficie')
        lebien.legislationbau=request.POST.get('legislationbau')
        lebien.delaispaiement=request.POST.get('delaispaiement')
        lebien.circonscription=request.POST.get('circonscription')
        lebien.revenumensuel=request.POST.get('revenumensuel')
        lebien.usage=request.POST.get('usage')
        lebien.commune=request.POST.get('commune')
        lebien.quartier=request.POST.get('quartier')
        lebien.proprietaire_id=request.POST.get('proprietaire')
        lebien.typebien=request.POST.get('typebien')
        lebien.caution=request.POST.get('caution')
        lebien.loyeravance=request.POST.get('loyeravance')
        lebien.cautioncie=request.POST.get('cautioncie')
        lebien.fraisagence=request.POST.get('fraisagence')
        lebien.enregistrementbail=request.POST.get('enregistrementbail')
        lebien.assurance=request.POST.get('assurance')
        lebien.fraisrenouvellement=request.POST.get('fraisrenouvellement')
        lebien.docs=request.POST.get('docs')
        lebien.save()
        return redirect ('espacebien')
    return render (request,'modifbien.html',context)

#Espace des biens
def espacebien(request):
    listebien=bien.objects.filter(status='valide')
    context={'listebien':listebien}
    return render(request,'espacebien.html',context)
    
#Composant des biens
def adcompbien(request,id):
    lebien=bien.objects.get(id=id)
    lesbien=bien.objects.all()
    context={'lebien':lebien,'lesbien':lesbien}
    if request.method=='POST':
        nomcomposant=request.POST.get('nomcomposant')
        nature=request.POST.get('nature')
        nbrepieces=request.POST.get('nbrepieces')
        descriptions=request.POST.get('descriptions')
        titreproprite=request.POST.get('titreproprite')
        numtitreproprite=request.POST.get('numtitreproprite')
        bien_id=lebien.id
        loyer=request.POST.get('loyer')
        superficie=request.POST.get('superficie')
        Statut=request.POST.get('Statut')
        caution=request.POST.get('caution')
        loyeravance=request.POST.get('loyeravance')
        cautioncie=request.POST.get('cautioncie')
        fraisagence=request.POST.get('fraisagence')
        depotgarantie=request.POST.get('depotgarantie')

        savecompo=compbien.objects.create(numtitreproprite=numtitreproprite,titreproprite=titreproprite,depotgarantie=depotgarantie,nomcomposant=nomcomposant,nbrepieces=nbrepieces,descriptions=descriptions,bien_id=bien_id,loyer=loyer,superficie=superficie,Statut=Statut,caution=caution,loyeravance=loyeravance,cautioncie=cautioncie,fraisagence=fraisagence,nature=nature)
        savecompo.save()
    return render(request,'adcompbien.html',context)

#Espace composants bien
def espacecompobien(request,id):
    lebien=compbien.objects.get(id=id)
    lescomposant=compbien.objects.filter(bien_id=lebien.id)
    context={'lebien':lebien,'lescomposant':lescomposant}
    return render(request,'espacecompobien.html',context)

#Ajout Locataire
def adclient (request):
    if request.method=='POST':
        nom=request.POST.get('nom')
        lieuhabitationactuelle=request.POST.get('lieuhabitationactuelle')
        situationmatrimoniale=request.POST.get('situationmatrimoniale')
        fonction=request.POST.get('fonction')
        besoin=request.POST.get('besoin')
        localite=request.POST.get('localite')
        contact1=request.POST.get('contact1')
        contact2=request.POST.get('contact2')
        budget=request.POST.get('budget')
        adressemail=request.POST.get('adressemail')
        commentaire=request.POST.get('commentaire')
        statut='Attente'
        datenaisloca=request.POST.get('datenaisloca')
        lieunaissloca=request.POST.get('lieunaissloca')
        naturepieceloca=request.POST.get('naturepieceloca')
        dateeditionpiece=request.POST.get('dateeditionpiece')
        datefinpiece=request.POST.get('datefinpiece')
        numpiece=request.POST.get('numpiece')
        lieueditionpiece=request.POST.get('lieueditionpiece')
        adressepostalloca=request.POST.get('adressepostalloca')
        nombreenfant=request.POST.get('nombreenfant')
        personnecasurgent=request.POST.get('personnecasurgent')
        nationnaliteloca=request.POST.get('contacturgence')
        contacturgence=request.POST.get('contacturgence')
        capital=request.POST.get('capital')
        representant=request.POST.get('representant')
        contact1representant=request.POST.get('contact1representant')
        mailrepesentant=request.POST.get('mailrepesentant')
        ncc=request.POST.get('ncc')
        rc=request.POST.get('rc')
        siegesocial=request.POST.get('siegesocial')
        genre=request.POST.get('genre')
        saveclient=client.objects.create(nom=nom,lieuhabitationactuelle=lieuhabitationactuelle,situationmatrimoniale=situationmatrimoniale,fonction=fonction,besoin=besoin,localite=localite,contact1=contact1,contact2=contact2,budget=budget,adressemail=adressemail,commentaire=commentaire,statut=statut,datenaisloca=datenaisloca,lieunaissloca=lieunaissloca,naturepieceloca=naturepieceloca,dateeditionpiece=dateeditionpiece,datefinpiece=datefinpiece,numpiece=numpiece,lieueditionpiece=lieueditionpiece,adressepostalloca=adressepostalloca,nombreenfant=nombreenfant,personnecasurgent=personnecasurgent,nationnaliteloca=nationnaliteloca,contacturgence=contacturgence,capital=capital,representant=representant,contact1representant=contact1representant,mailrepesentant=mailrepesentant,ncc=ncc,rc=rc,siegesocial=siegesocial,genre=genre)
        saveclient.save()
        return redirect ('prospectclient')
    return render (request, 'adclient.html')

#ESPACE Locataire Prospect
def prospectclient(request):
    listeprospectclient=client.objects.filter(statut='Attente')
    context={'listeprospectclient':listeprospectclient}
    return render (request, 'prospectclient.html',context)

#Espace Locataire
def espaceclient(request):
    lesclients=client.objects.filter(statut='valide')
    context={'lesclients':lesclients}
    return render (request, 'espaceclient.html', context)

#Modif client
def modifclient(request,id):
    leclient=client.objects.get(id=id)
    listestatus=status.objects.all()
    context={'leclient':leclient,'listestatus':listestatus}
    if request.method=='POST':
        leclient.nom=request.POST.get('nom')
        leclient.lieuhabitationactuelle=request.POST.get('lieuhabitationactuelle')
        leclient.situationmatrimoniale=request.POST.get('situationmatrimoniale')
        leclient.fonction=request.POST.get('fonction')
        leclient.datecreation=leclient.datecreation
        leclient.besoin=request.POST.get('besoin')
        leclient.localite=request.POST.get('localite')
        leclient.contact1=request.POST.get('contact1')
        leclient.contact2=request.POST.get('contact2')
        leclient.budget=request.POST.get('budget')
        leclient.adressemail=request.POST.get('adressemail')
        leclient.commentaire=request.POST.get('commentaire')
        leclient.statut=request.POST.get('statut')
        leclient.datenaisloca=request.POST.get('datenaisloca')
        leclient.lieunaissloca=request.POST.get('lieunaissloca')
        leclient.naturepieceloca=request.POST.get('naturepieceloca')
        leclient.dateeditionpiece=request.POST.get('dateeditionpiece')
        leclient.datefinpiece=request.POST.get('datefinpiece')
        leclient.numpiece=request.POST.get('numpiece')
        leclient.lieueditionpiece=request.POST.get('lieueditionpiece')
        leclient.adressepostalloca=request.POST.get('adressepostalloca')
        leclient.nombreenfant=request.POST.get('nombreenfant')
        leclient.personnecasurgent=request.POST.get('personnecasurgent')
        leclient.nationnaliteloca=request.POST.get('contacturgence')
        leclient.contacturgence=request.POST.get('contacturgence')
        leclient.capital=request.POST.get('capital')
        leclient.representant=request.POST.get('representant')
        leclient.contact1representant=request.POST.get('contact1representant')
        leclient.mailrepesentant=request.POST.get('mailrepesentant')
        leclient.ncc=request.POST.get('ncc')
        leclient.rc=request.POST.get('rc')
        leclient.siegesocial=request.POST.get('siegesocial')
        leclient.genre=request.POST.get('genre')
        leclient.save()
        return redirect ('espaceclient')
    return render (request, 'modifclient.html', context)


def adcontrat(request):
    lescommerciaux=newuser.objects.all()
    lesclients=client.objects.filter(statut='valide')
    lespieces=compbien.objects.all()
    lesbiens=bien.objects.all()
    context={'lescommerciaux':lescommerciaux,'lesclients':lesclients,'lespieces':lespieces,'lesbiens':lesbiens}
    #id_piece=request.GET.get("pieces")
    
    if request.method== "POST":
        if request.user.is_authenticated:
            typebail=request.POST.get('typebail')
            client_id=request.POST.get('client_id')
            bien_id=request.POST.get('lesbiens')
            compbien_id=request.POST.get('app')
            newuser_id=request.user.id
            datedebut=request.POST.get('debut')
            datefin=request.POST.get('fin')
            dureecontrat=request.POST.get('dureecontrat')
            datedernierreglement=request.POST.get('datedernierreglement')
            dateprochainreglement=request.POST.get('dateprochainreglement')
            delaispaiement=request.POST.get('delaispaiement')
            loyer=request.POST.get('loyer')
            loyeravance=request.POST.get('loyeravance')
            penalite=request.POST.get('penalite')
            depotgarantie=request.POST.get('depotgarantie')
            fraisagence=request.POST.get('fraisagence')
            caution=request.POST.get('caution')
            cautioncie=request.POST.get('cautioncie')
            statut='Attente'
            commentaire=request.POST.get('commentaire')
            savecontrat=contrat.objects.create(typebail=typebail,client_id=client_id,bien_id=bien_id,compbien_id=compbien_id,newuser_id=newuser_id,datedebut=datedebut,datefin=datefin,dureecontrat=dureecontrat,datedernierreglement=datedernierreglement,dateprochainreglement=dateprochainreglement,delaispaiement=delaispaiement,loyer=loyer,loyeravance=loyeravance,penalite=penalite,depotgarantie=depotgarantie,fraisagence=fraisagence,caution=caution,cautioncie=cautioncie,statut=statut,commentaire=commentaire)
            savecontrat.save()
            return redirect (prospectcontrat)

        else:
            print("Veuillez vous connecter")
            return redirect (conex)
    return render (request,'adcontrat.html',context)

    # if id_piece:
    #     lapiece=compbien.objects.get(id=id_piece)
    #     #Le formulaire de recuperation des biens et leurs composants
    #     form_b=biensForm()
    #     #formp=formpieces(initial={'nomcomposant':lapiece})
    #     form_c=composantsForm(instance=lapiece)
    # else:
    #     lapiece=compbien.objects.get(id=1)
    #     print(lapiece)
    #     form_b=biensForm()
    #     form_c=composantsForm(instance=lapiece)
 



#PROSPECT CONTRATS
def prospectcontrat (request):
    lescontrats=contrat.objects.filter(statut='Attente')
    context={'lescontrats':lescontrats}
    return render (request, 'prospectcontrat.html',context)


#Espace contrat
def espacecontrat (request):
    lescontrats=contrat.objects.filter(statut='valide')
    context={'lescontrats':lescontrats}
    return render (request, 'espacecontrat.html',context)

# Espace superadmin
def espaceadmin(request):
    form_b=biensForm()
    context={'form_b':form_b}
    return render(request,'superuserpage.html',context)



#Load pieces
def load_piece(request):
    bien_id=request.GET.get("biens")
    lespieces=compbien.objects.filter(bien_id=bien_id)
    context={'lespieces':lespieces,'bien_id':bien_id}
    return render (request,"piece_option.html", context)


#Load pieces
def load_piece_details(request):
    id_compbien=request.GET.get("npieces")
    lapiece=compbien.objects.filter(id=id_compbien)
    context={'lapiece':lapiece,'id_compbien':id_compbien}
    return render (request,"piece_option_details.html", context)


def sample_data(request):
    if request.method=='POST':
        province = request.POST['list1']
        print(province) #return ex. 2 depend on select value
    return render (request,'sample.html')


def test(request):
    form=formtest()
    context={'form':form}
    if request.method =="POST":
        text=request.POST.get("text")
        photo=request.POST.get("photo")
        doc=request.POST.get("doc")
        savetest=tests.objects.create(text=text, photo=photo, doc=doc)
        savetest.save()
    # if request.method =='POST':
    #     form=formtest(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         context={'form':form}
    #         print("form is not valid")
    #         return render (request,'test.html',context)
    # context={'form':formtest()}
    return render (request,'test.html',context)


    #API
def apicompbien(request):
    data=compbien.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, 'nomcomposant':i.nomcomposant, 'loyer':i.loyer, 'descriptions':i.descriptions, 'bien_id':i.bien_id, 'fraisagence':i.fraisagence, 'depotgarantie':i.depotgarantie, 'datecreation':i.datecreation, 'Statut':i.Statut, 'superficie':i.superficie, 'nature':i.nature, 'nbrepieces':i.nbrepieces, 'caution':i.caution, 'loyeravance':i.loyeravance, 'cautioncie':i.cautioncie})
    return JsonResponse(datalist, safe=False)


    #API PRRESTATIONS
def apiprestation(request):
    data=prestations.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, 'description':i.description, 'montant':i.montant})
    return JsonResponse(datalist, safe=False)

@csrf_exempt
def createTest(request):
    description=request.POST.get('description')
    montant=request.POST.get('montant')
    prestations.objects.create(description=description,montant=montant)
    return JsonResponse('Test created!', safe=False)

def adprofm(request, idproprietaire):
    lepersonnel=personnel.objects.all()
    lesbiens=bien.objects.all()
    lespres=prestations.objects.all()
    leproprio=proprietaire.objects.get(id=idproprietaire)
    context={'leproprio':leproprio, 'lesbiens':lesbiens,'lespres':lespres,'lepersonnel':lepersonnel}
    if request.method=="POST":
        proprietaire_id=leproprio.id
        numquitance=  request.POST.get("numquitance")
        delaispaiement=  request.POST.get("delaispaiement")
        bien_id=request.POST.get("bien")
        usage= request.POST.get("usage")
        personnel_id=request.POST.get("commercial")
        soustotal= request.POST.get("soustotal")
        totaltva=request.POST.get("totaltva")
        totalttc=request.POST.get("totalttc")
        remise=request.POST.get("remise")
        netapayer=request.POST.get("netapayer")
        typeproforma="mandat" 
        dateedition=request.POST.get("datecreation")
        saveproforma=proforma.objects.create(dateedition=dateedition,usage=usage,proprietaire_id=proprietaire_id,numquitance=numquitance,delaispaiement=delaispaiement,bien_id=bien_id,typeproforma=typeproforma,personnel_id=personnel_id,soustotal=soustotal,totaltva=totaltva,totalttc=totalttc,remise=remise,netapayer=netapayer)
        saveproforma.save()
        return redirect('espaceproform')
    return render (request, 'adprofm.html',context)


#Liste des proforma de mandat da gestion
def espaceproform(request):
    lesproformam=proforma.objects.filter(typeproforma="mandat")
    context={'lesproformam':lesproformam}
    return render (request,'espaceproform.html',context)


#Details proforma mandat
def detailprofm(request, idprof):
    lespres=prestations.objects.all()
    laproforma=proforma.objects.get(id=idprof)
    lesdetailsprof=detailsproforma.objects.filter(proforma_id=idprof)
    context={'lesdetailsprof':lesdetailsprof,'laproforma':laproforma,'lespres':lespres}
    if request.method== 'POST':
            typeproforma=request.POST.get('')
            proforma_id=laproforma.id
            prestations_id=request.POST.get('description')
            soustotal=request.POST.get('montant')
            totaltva=request.POST.get('totaltva')
            totalttc=request.POST.get('totalttc')
            remise=request.POST.get('remise')
            netapayer=request.POST.get('netapayer')
            savedetails=detailsproforma.objects.create(typeproforma=typeproforma,proforma_id=proforma_id,prestations_id=prestations_id,soustotal=soustotal,totaltva=totaltva,totalttc=totalttc,remise=remise,netapayer=netapayer)
            savedetails.save()

            #Modification de la proforma
            laproforma.soustotal=laproforma.soustotal+int(request.POST.get('montant'))
            laproforma.totaltva=laproforma.totaltva+int(request.POST.get('totaltva'))
            laproforma.totalttc=laproforma.totalttc+int(request.POST.get('totalttc'))
            laproforma.loyer=laproforma.loyer+int(request.POST.get('totalttc'))
            laproforma.remise=laproforma.remise+int(request.POST.get('remise'))
            laproforma.netapayer=laproforma.netapayer+int(request.POST.get('netapayer'))
            laproforma.resteapayer=laproforma.resteapayer+int(request.POST.get('netapayer'))
            laproforma.save()
    return render(request,'detailprofm.html',context)

#Suppression de detail de proforma
def supligneprof(request,idligne):
    laligne=detailsproforma.objects.get(id=idligne)
    idproforma=laligne.proforma_id
    laproforma=proforma.objects.get(id=idproforma)
    context={'laligne':laligne,'laproforma':laproforma}
    if request.method=='POST':
        #Modification de la proforma
        laproforma.soustotal=laproforma.soustotal-laligne.soustotal
        laproforma.totaltva=laproforma.totaltva-laligne.totaltva
        laproforma.totalttc=laproforma.totalttc-laligne.totalttc
        laproforma.loyer=laproforma.loyer-laligne.totalttc
        laproforma.remise=laproforma.remise-laligne.remise
        laproforma.netapayer=laproforma.netapayer-laligne.netapayer
        laproforma.resteapayer=laproforma.resteapayer-laligne.netapayer
        laproforma.save()
        #Suppresion de la ligne
        laligne.delete()
        return redirect ("/detailprofm/"+str(idproforma))
    return render(request,'sup.html',context)



        

    #API PRRESTATIONS
def apidetailsprof(request):
    data=detailsproforma.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, 'typeproforma':i.typeproforma, 'proforma_id':i.proforma_id,'description':i.description, 'soustotal':i.soustotal, 'totaltva':i.totaltva, 'totalttc':i.totalttc,'remise':i.remise, 'netapayer':i.netapayer})
    return JsonResponse(datalist, safe=False)


#IMPRESSION PROFORMA MANDAT
def etatprofm_old(request, idprof):
    laproforma=proforma.objects.get(id=idprof)
    leslignes=detailsproforma.objects.filter(proforma_id=idprof)
    leproprio=proprietaire.objects.filter(id=laproforma.proprietaire_id)
    #context=get_invoice(pk)
    context={'leslignes':leslignes,'laproforma':laproforma,'leproprio':leproprio}
    #context['date']=datetime.datetime.today()
    template=get_template('etatprofm.html')
    #Envoi des informations dans le fichier html
    html=template.render(context)

    #Les options du pdf
    options = {
    'page-size': 'letter',
    'encoding': "UTF-8"
}
    
    #Generation du pdf
    pdf=pdfkit.from_string(html,False,options)
    Response=HttpResponse(pdf,content_type='application/pdf')
    Response['Content-Disposition']="attachment"

    return(Response)

def etatprofm(request,idprof):
    laproforma=proforma.objects.get(id=idprof)
    leslignes=detailsproforma.objects.filter(proforma_id=idprof)
    leproprio=proprietaire.objects.filter(id=laproforma.proprietaire_id)
    netenletre=num2words(laproforma.netapayer,lang='fr')
    #context=get_invoice(pk)
    context={'leslignes':leslignes,'laproforma':laproforma,'leproprio':leproprio,'netenletre':netenletre}
    template_path = 'etatprofm.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="PROFORMA_MANDAT.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


#Ajout facture mandat
def adfactm(request, idprof):
    listestatus=status.objects.all()
    laproforma=proforma.objects.get (id=idprof)
    lesdetails=detailsproforma.objects.filter(proforma_id=idprof)
    context={'laproforma':laproforma,'lesdetails':lesdetails,'listestatus':listestatus}
    if request.method=='POST':
        typefacture="Mandat"
        proprietaire_id=laproforma.proprietaire_id
        proforma_id=laproforma.id
        bien_id=laproforma.bien_id
        localisation=request.POST.get('localisation')
        reference=request.POST.get('reference')
        datefacture=datetime.today()
        doit=laproforma.doit
        soustotal=laproforma.soustotal
        totaltva=laproforma.totaltva
        totalttc=laproforma.totalttc
        loyer=laproforma.loyer
        delaispaiement=laproforma.delaispaiement
        editepar=""
        dateedition=datetime.today()
        numquitance=laproforma.numquitance
        nature=laproforma.nature
        montantregle=0
        montantpenalite=0
        netapayer=laproforma.netapayer
        resteapayer=laproforma.resteapayer
        status_id=request.POST.get('statut')
        savefact=facture.objects.create(bien_id=bien_id,proprietaire_id=proprietaire_id,typefacture=typefacture,localisation=localisation,reference=reference,datefacture=datefacture,doit=doit,soustotal=soustotal,totaltva=totaltva,totalttc=totalttc,loyer=loyer,delaispaiement=delaispaiement,editepar=editepar,dateedition=dateedition,numquitance=numquitance,nature=nature, montantregle=montantregle, montantpenalite=montantpenalite,netapayer=netapayer,resteapayer=resteapayer,status_id=status_id)
        savefact.save()
        for detprof in lesdetails:
                facture_id=savefact.id
                proforma_id=laproforma.id
                description=detprof.prestations_id
                soustotal=detprof.soustotal
                totaltva=detprof.totaltva
                totalttc=detprof.totalttc
                remise=detprof.remise
                netapayer=detprof.netapayer
                savedetails=detailsfacture.objects.create(facture_id=facture_id,proforma_id=proforma_id,description=description,soustotal=soustotal,totaltva=totaltva,totalttc=totalttc,remise=remise,netapayer=netapayer)
                savedetails.save()
    return render (request, 'adfactm.html', context)

#ESPACE FACTURES
def espacefacturem(request):
    lesfactures=facture.objects.all()
    context={'lesfactures':lesfactures}
    return render (request,'espacefacturem.html',context)

#Ajout Reglement
def adreglementm(request, idfac):
    listestatus=status.objects.all()
    listemode=modereglement.objects.all()
    lafacture=facture.objects.get(id=idfac)
    context={'lafacture':lafacture,'listestatus':listestatus,'listemode':listemode}

    if request.method=='POST':
        facture_id=lafacture.id
        proforma_id=lafacture.proforma_id
        proprietaire_id=lafacture.proprietaire_id
        bien_id=lafacture.bien_id
        status_id=request.POST.get('statut')
        modereglement_id=request.POST.get('modereglement')
        datereg=request.POST.get('datereglement')
        montantregle=request.POST.get('paiementactuel')
        reste=request.POST.get('solde')
        commentaire=request.POST.get('commentaire')
        savereglement=regfactm.objects.create(status_id=status_id,facture_id=facture_id,proforma_id=proforma_id,proprietaire_id=proprietaire_id, bien_id=bien_id,modereglement_id=modereglement_id,datereg=datereg,montantregle=montantregle,reste=reste,commentaire=commentaire)
        savereglement.save()

        #Modification de la facure
        lafacture.montantregle=request.POST.get('totalreglementactuel')
        lafacture.resteapayer=request.POST.get('solde')
        lafacture.save()
        return redirect ('espacefacturem')
    return render(request,'adreglementm.html',context)
