from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.timezone import datetime
from django.forms import ModelChoiceField

#TEST
class tests(models.Model):
    text=models.CharField(max_length=100,default="")
    photo=models.ImageField(upload_to='imagetest/', blank=True, default='')
    doc=models.FileField(upload_to='filetest/', blank=True, default='')

    def _str_(self):
        return self.text
    

#CREATION DES UTILISATEURS AVEC DES CHAMPS SUPPLEMENTAIRES
class personnel(models.Model):
    Genre_Type=(( 'Homme','Homme'),('Femme', 'Femme'),('Autre', 'Autre'),)
    nom=models.CharField(max_length=200)
    contact=models.CharField(max_length=20)
    admail=models.EmailField(max_length=50)
    fonction=models.CharField(max_length=200)
    genre=models.CharField(max_length=10,choices=Genre_Type)
    photoid=models.ImageField(default="",null=True)

    class Meta:
        verbose_name=("Personne")
        verbose_name_plural=("Personnels")

#Lignes de devis
class prestations(models.Model):
    description=models.CharField( max_length=105, default=0)
    montant=models.BigIntegerField(default=0)
    
    def _str_(self):
        return self.description



#Type piece
class typepiece(models.Model):
    libel=models.CharField(max_length=100,default="")

#Type docs
class typedoc(models.Model):
    libelle=models.CharField(max_length=100)

#Status
class status(models.Model):
    libelle=models.CharField(max_length=100)

#Mode reglement
class modereglement(models.Model):
    libelle=models.CharField(max_length=50)

#Nature Contrat
class naturecontrat(models.Model):
    libelle=models.CharField(max_length=50)


# Structure.
class entite(models.Model):
    nom=models.CharField(max_length=100),
    tel=models.CharField(max_length=20),
    slogan=models.CharField(max_length=100) ,
    logo=models.ImageField(),
    representant=models.CharField(max_length=50) ,
    telrepre=models.CharField(max_length=20) ,
    emailrepre=models.CharField(max_length=50) ,
    fonctionrepre=models.CharField(max_length=50) ,
    localisation=models.CharField(max_length=150) ,
    adressepostal=models.CharField(max_length=100) ,
    capital=models.IntegerField(default=0) ,
    siege=models.CharField(max_length=100),
    regime=models.CharField(max_length=40),
    siteweb=models.CharField(max_length=50),
    emailstructure=models.CharField(max_length=50),
    rcc=models.CharField(max_length=50),
    ncc=models.CharField(max_length=50),
    proprietaire=models.CharField(max_length=100)

    class Meta:
        verbose_name=("User")
        verbose_name_plural=("Users")

#SURCHARGE POUR AFFICHER LES VALEURS DANS LE TABLEAU DE L'ESPACE ADMIN 
def _str_(self):
    return self.name


#CREATION DES UTILISATEURS AVEC DES CHAMPS SUPPLEMENTAIRES
class newuser(models.Model):
    Genre_Type=(( 'Homme','Homme'),('Femme', 'Femme'),('Autre', 'Autre'),)

    nom=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=20)
    admail=models.EmailField(max_length=50)
    localisation=models.CharField(max_length=200)
    genre=models.CharField(max_length=10,choices=Genre_Type)
    photoid=models.ImageField(default="")

    class Meta:
        verbose_name=("New User")
        verbose_name_plural=("New Users")

def _str_(self):
    return self.name


#Proprietaire
class proprietaire(models.Model):
    genre=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    fonctions=models.CharField(max_length=50, null=True)
    numpiece=models.CharField(max_length=50, null=True)
    contact1=models.CharField(max_length=50, null=True)
    contact2=models.CharField(max_length=50, null=True)
    lieuhabitation=models.CharField(max_length=50, null=True)
    photo=models.ImageField(null=True)
    adressemail=models.CharField(max_length=50, null=True)
    naturepiece=models.CharField(max_length=50, null=True)
    situationmatrimoniale=models.CharField(max_length=50, null=True)
    personneurgence=models.CharField(max_length=50, null=True)
    contacturgence=models.CharField(max_length=50, null=True)
    datenais=models.DateField(default="")
    datevalidepiece=models.DateField(default="")
    lieunaissance=models.CharField(max_length=50, null=True)
    nationnalite=models.CharField(max_length=50, null=True)
    representant=models.CharField(max_length=50, null=True)
    contact1representant=models.CharField(max_length=50, null=True)
    numcompte=models.CharField(max_length=50, null=True)
    boitepostale=models.CharField(max_length=50, null=True)
    statut=models.CharField(max_length=50, null=True)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)

    def _str_(self):
        return self.nom

    class Meta:
        verbose_name=("Proprietaire")
        verbose_name_plural=("Proprietaires")




#le bien
class bien(models.Model):
    nom=models.CharField(max_length=50)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)
    localisation=models.CharField(max_length=50, null=True)
    commentaire=models.CharField(max_length=100, null=True)
    lot=models.IntegerField(default="",null=True)
    iLot=models.IntegerField(default="",null=True)
    titreproprite=models.CharField(max_length=100,null=True)
    numtitreproprite=models.CharField(max_length=100,null=True)
    superficie=models.BigIntegerField(default=0, null=True)
    legislationbau=models.IntegerField(default=0, null=True)
    delaispaiement=models.IntegerField(default=0, null=True)
    status=models.CharField(max_length=50, null=True)
    circonscription=models.CharField(max_length=100,null=True)
    revenumensuel=models.BigIntegerField(default=50, null=True)
    usage=models.CharField(max_length=50, null=True)
    commune=models.CharField(max_length=50, null=True)
    quartier=models.CharField(max_length=50, null=True)
    proprietaire=models.ForeignKey(proprietaire, on_delete=models.CASCADE)
    typebien=models.CharField(max_length=50, null=True)
    caution=models.IntegerField(null=True) 
    loyeravance=models.IntegerField(default=0,null=True) 
    cautioncie=models.IntegerField(default=0,null=True) 
    fraisagence=models.IntegerField(default=0, null=True) 
    enregistrementbail=models.IntegerField(default=0, null=True) 
    assurance=models.IntegerField(null=True, default=0) 
    fraisrenouvellement=models.IntegerField(default=0,null=True) 
    docs=models.FileField(upload_to="documents",null=True, default="")

    def _str_(self):
        return self.nom

    
    #Permet de recuperer les valeurs à afficher dans un select modelform dans le fichier form.py
    class NameChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            #return f'{obj.nom} {obj.nom}'
            return f'{obj.nom}'


#Les composants du site
class compbien(models.Model):
    nomcomposant=models.CharField(max_length=50)
    nature=models.CharField(max_length=50)
    nbrepieces=models.IntegerField(null=True)
    descriptions=models.CharField(max_length=200, null=True)
    bien=models.ForeignKey(bien, on_delete=models.CASCADE)
    loyer=models.IntegerField( null=True)
    superficie=models.IntegerField(null=True)
    Statut=models.CharField(max_length=50, null=True)
    caution=models.IntegerField( null=True)
    loyeravance=models.IntegerField(null=True)
    cautioncie=models.IntegerField(null=True)
    fraisagence=models.IntegerField( null=True)
    depotgarantie=models.IntegerField( null=True)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)


    def _str_(self):
     return self.nomcomposant

    class NameChoiceFieldpiece(ModelChoiceField):
        def label_from_instance(self, obj):
            #return f'{obj.nom} {obj.nom}'
            return f'{obj.nomcomposant}'


#Client
class client(models.Model):
    nom=models.CharField(max_length=100)
    lieuhabitationactuelle=models.CharField(max_length=100, null=True)
    situationmatrimoniale=models.CharField(max_length=50, null=True)
    fonction=models.CharField(max_length=50, null=True)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)
    besoin=models.CharField(max_length=200, null=True)
    localite=models.CharField(max_length=200, null=True)
    contact1=models.CharField(max_length=50)
    contact2=models.CharField(max_length=50, null=True)
    budget=models.IntegerField(default=0)
    adressemail=models.EmailField(max_length=50, null=True)
    commentaire=models.CharField(max_length=200, null=True)
    statut=models.CharField(max_length=50, null=True)
    datenaisloca=models.DateField( null=True)
    lieunaissloca=models.CharField(max_length=50, null=True)
    naturepieceloca=models.CharField(max_length=50, null=True)
    dateeditionpiece=models.DateField(null=True)
    datefinpiece=models.DateField( null=True)
    numpiece=models.CharField(max_length=50, null=True)
    lieueditionpiece=models.CharField(max_length=50, null=True)
    adressepostalloca=models.CharField(max_length=50, null=True)
    nombreenfant=models.IntegerField(default=0, null=True)
    personnecasurgent=models.CharField(max_length=50, null=True)
    nationnaliteloca=models.CharField(max_length=50, null=True)
    contacturgence=models.CharField(max_length=50, null=True)
    capital=models.BigIntegerField(default=0, null=True)
    representant=models.CharField(max_length=50, null=True)
    contact1representant=models.CharField(max_length=50, null=True)
    mailrepesentant=models.EmailField(null=True)
    ncc=models.CharField(max_length=50, null=True)
    rc=models.CharField(max_length=50, null=True)
    siegesocial=models.CharField(max_length=50, null=True)
    genre=models.CharField(max_length=50)

    
    def _str_(self):
        return self.nom

    class Meta:
        verbose_name=("Client")
        verbose_name_plural=("Clients")


#contrat de bail
class contrat(models.Model):
    typebail=models.CharField(max_length=50, null=False)
    datecration=models.DateTimeField(default=datetime.now, blank=True)
    client=models.ForeignKey(client,on_delete=models.CASCADE, null=False)
    bien=models.ForeignKey(bien,on_delete=models.CASCADE, null=False)
    compbien=models.ForeignKey(compbien,on_delete=models.CASCADE, null=False)
    newuser=models.ForeignKey(newuser,on_delete=models.CASCADE, null=False)
    datedebut=models.DateField(default="", null=True)
    datefin=models.DateField(default="", null=True)
    dureecontrat=models.CharField(max_length=50,default="", null=True)
    datedernierreglement=models.DateField(default=0, null=True)
    dateprochainreglement=models.DateField(default=0, null=True)
    delaispaiement=models.IntegerField(default="", null=True)
    loyer=models.BigIntegerField(default=0, null=True)
    loyeravance=models.BigIntegerField(default=0, null=True)
    penalite=models.BigIntegerField(default=0, null=True)
    depotgarantie=models.IntegerField(default=0, null=True)
    fraisagence=models.BigIntegerField(default=0, null=True)
    caution=models.BigIntegerField(default=0, null=True)
    cautioncie=models.BigIntegerField(default=0, null=True)
    statut=models.CharField(max_length=50, default="")
    commentaire=models.CharField(max_length=500, null=True, default="")


    class Meta:
        verbose_name=("Contrat")
        verbose_name_plural=("Contrats")


#PROFORMA
class proforma(models.Model):
    typeproforma=models.CharField(max_length=50, null=True)
    bien=models.ForeignKey(bien,on_delete=models.CASCADE, null=False)
    personnel=models.ForeignKey(personnel,on_delete=models.CASCADE, null=False)
    proprietaire=models.ForeignKey(proprietaire,on_delete=models.CASCADE, null=False)
    dateproforma=models.DateField(default=date.today)
    doit=models.CharField(max_length=50, null=True)
    soustotal=models.BigIntegerField(default=0, null=True)
    totaltva=models.BigIntegerField(default=0, null=True)
    totalttc=models.BigIntegerField(default=0, null=True)
    loyer=models.BigIntegerField(default=0, null=True)
    remise=models.BigIntegerField(default=0, null=True)
    netapayer=models.BigIntegerField(default=0, null=True)
    delaispaiement=models.DateField(default="", null=True, blank=True)
    editepar=models.CharField(max_length=50, null=True)
    dateedition=models.DateField(default="", null=True, blank=True)
    numquitance=models.CharField(max_length=50, null=True)
    nature=models.CharField(max_length=50, null=True)
    usage=models.CharField(max_length=50, null=True)
    montantregle=models.BigIntegerField(default=0, null=True)
    resteapayer=models.BigIntegerField(default=0, null=True)
    status=models.CharField(max_length=50, null=True)
    observation=models.CharField(default="",max_length=200, null=True)


    class Meta:
        verbose_name=("Proforma")
        verbose_name_plural=("Proformas")


#DETAILS PROFORMA
class detailsproforma(models.Model):
    typeproforma=models.CharField(max_length=50, null=True)
    proforma=models.ForeignKey(proforma,on_delete=models.CASCADE, null=False)
    prestations=models.ForeignKey(prestations,on_delete=models.CASCADE, null=False)
    soustotal=models.BigIntegerField(default=0, null=True)
    totaltva=models.BigIntegerField(default=0, null=True)
    totalttc=models.BigIntegerField(default=0, null=True)
    remise=models.BigIntegerField(default=0, null=True)
    netapayer=models.BigIntegerField(default=0, null=True)

    class Meta:
        verbose_name=("detailproforma")
        verbose_name_plural=("detailproformas")

def _str_(self):
    return self.description



#Factures
class facture(models.Model):
    typefacture=models.CharField(max_length=50, null=True)
    localisation=models.CharField(max_length=50, null=True)
    reference=models.CharField(max_length=50)
    datefacture=models.DateField(default=date.today)
    doit=models.CharField(max_length=50, null=True)
    soustotal=models.BigIntegerField(default=0, null=True)
    totaltva=models.BigIntegerField(default=0, null=True)
    totalttc=models.BigIntegerField(default=0, null=True)
    loyer=models.BigIntegerField(default=0, null=True)
    delaispaiement=models.DateField(default=date.today)
    editepar=models.CharField(max_length=50, null=True)
    dateedition=models.DateField(default="", null=True)
    numquitance=models.CharField(max_length=50, null=True)
    nature=models.CharField(max_length=50, null=True)
    montantregle=models.BigIntegerField(default=0, null=True)
    montantpenalite=models.BigIntegerField(default=0, null=True)
    netapayer=models.BigIntegerField(default=0, null=True)
    resteapayer=models.BigIntegerField(default=0, null=True)
    status=models.ForeignKey(status,on_delete=models.CASCADE)
    proprietaire=models.ForeignKey(proprietaire,on_delete=models.CASCADE)
    proforma=models.ForeignKey(proforma,on_delete=models.CASCADE)
    bien=models.ForeignKey(bien,on_delete=models.CASCADE)




    class Meta:
        verbose_name=("Facture")
        verbose_name_plural=("Factures")



#Details factures
class detailsfacture(models.Model):
    facture=models.ForeignKey(facture,on_delete=models.CASCADE, null=False)
    proforma=models.ForeignKey(proforma,on_delete=models.CASCADE, null=False)
    description=models.CharField(max_length=100, null=True)
    soustotal=models.BigIntegerField(default=0, null=True)
    totaltva=models.BigIntegerField(default=0, null=True)
    totalttc=models.BigIntegerField(default=0, null=True)
    remise=models.BigIntegerField(default=0, null=True)
    netapayer=models.BigIntegerField(default=0, null=True)

    class Meta:
        verbose_name=("detailfacture")
        verbose_name_plural=("detailfactures")


#MANDAT DE GESTION APRES REGLEMENT DE LA FACTURE PROFORMA ACCEPTEE PAR LE PROPRIETAIRE
class mandat(models.Model):
    typemandat=models.CharField(max_length=50, null=False)
    datecration=models.DateTimeField(default=datetime.now, blank=True)
    proprietaire=models.ForeignKey(proprietaire,on_delete=models.CASCADE, null=False)
    bien=models.ForeignKey(bien,on_delete=models.CASCADE, null=False)
    facture=models.ForeignKey(facture,on_delete=models.CASCADE, null=False)
    newuser=models.ForeignKey(newuser,on_delete=models.CASCADE, null=False)
    datedebut=models.DateField(default="", null=True)
    datefin=models.DateField(default="", null=True)
    dureecontrat=models.CharField(max_length=50,default="", null=True)
    delaispaiement=models.IntegerField(default="", null=True)
    revenumensuel=models.BigIntegerField(default=0, null=True)
    fraisdossier=models.BigIntegerField(default=0, null=True)
    statut=models.CharField(max_length=50, default="")
    commentaire=models.CharField(max_length=500, null=True, default="")

    class Meta:
        verbose_name=("mandat")
        verbose_name_plural=("mandats")
  

#LIGNE DE Reglement
class regfactm(models.Model):
    facture=models.ForeignKey(facture,on_delete=models.CASCADE,default="",null=True)
    proforma=models.ForeignKey(proforma,on_delete=models.CASCADE,default="",null=True)
    proprietaire=models.ForeignKey(proprietaire,on_delete=models.CASCADE,default="",null=True)
    bien=models.ForeignKey(bien,on_delete=models.CASCADE,default="",null=True)
    status=models.ForeignKey(status,on_delete=models.CASCADE,default="",null=True)
    modereglement=models.ForeignKey(modereglement,on_delete=models.CASCADE)
    datereg=models.DateField(default=datetime.today)
    montantregle=models.IntegerField(default=0)
    reste=models.IntegerField(default=0)
    commentaire=models.CharField(max_length=500, default="")

    class Meta:
        verbose_name=("Reglement Mandat")
        verbose_name_plural=("Reglement Mandat")




