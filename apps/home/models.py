# -*- encoding: utf-8 -*-

from django.db import models


class DimCategorie(models.Model):
    categorieid = models.IntegerField(db_column='CategorieID', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=9, blank=True, null=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_Categorie'


class DimDate(models.Model):
    dateid = models.IntegerField(db_column='DateID', primary_key=True)  # Field name made lowercase.
    date = models.DateField()
    code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Dim_Date'


class DimEmployee(models.Model):
    id_employee = models.IntegerField(db_column='ID_Employee', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=1, blank=True, null=True)  # Field name made lowercase.
    datenaissance = models.DateField(db_column='DateNaissance', blank=True, null=True)  # Field name made lowercase.
    lieunaissance = models.CharField(db_column='LieuNaissance', max_length=16, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(db_column='Ville', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codepostal = models.IntegerField(db_column='CodePostal', blank=True, null=True)  # Field name made lowercase.
    nbenfant = models.IntegerField(db_column='NbEnfant', blank=True, null=True)  # Field name made lowercase.
    salairebase = models.FloatField(db_column='SalaireBase', blank=True, null=True)  # Field name made lowercase.
    banque = models.CharField(db_column='Banque', max_length=50, blank=True, null=True)  # Field name made lowercase.
    daterecrutement = models.DateField(db_column='DateRecrutement', blank=True, null=True)  # Field name made lowercase.
    datedebutcontrat = models.DateField(db_column='DateDebutContrat', blank=True, null=True)  # Field name made lowercase.
    dureecontrat = models.IntegerField(db_column='DureeContrat', blank=True, null=True)  # Field name made lowercase.
    poste = models.CharField(db_column='Poste', max_length=12, blank=True, null=True)  # Field name made lowercase.
    montantrend = models.FloatField(db_column='MontantRend', blank=True, null=True)  # Field name made lowercase.
    noteabsence = models.FloatField(db_column='NoteAbsence', blank=True, null=True)  # Field name made lowercase.
    nbrabsence = models.IntegerField(db_column='NbrAbsence', blank=True, null=True)  # Field name made lowercase.
    noteassiduite = models.FloatField(db_column='NoteAssiduite', blank=True, null=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quitter = models.CharField(db_column='Quitter', max_length=1, blank=True, null=True)  # Field name made lowercase.
    datequitter = models.DateField(db_column='DateQuitter', blank=True, null=True)  # Field name made lowercase.
    motifquitter = models.CharField(db_column='MotifQuitter', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_Employee'


class DimEtatcivil(models.Model):
    id_etatcivil = models.IntegerField(db_column='ID_EtatCivil', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_EtatCivil'


class DimFonction(models.Model):
    id_fonction = models.IntegerField(db_column='ID_Fonction', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=38)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_Fonction'


class DimJours(models.Model):
    field_id = models.IntegerField(db_column='_ID', primary_key=True)  # Field name made lowercase. Field renamed because it started with '_'.
    jour = models.CharField(db_column='Jour', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_Jours'


class DimModepaiement(models.Model):
    id_modepaiement = models.IntegerField(db_column='ID_ModePaiement', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_ModePaiement'


class DimMois(models.Model):
    field_id_mois = models.IntegerField(db_column='_ID_Mois', primary_key=True)  # Field name made lowercase. Field renamed because it started with '_'.
    mois = models.CharField(db_column='Mois', max_length=11, blank=True, null=True)  # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_Mois'


class DimMotifconge(models.Model):
    id_motifconge = models.IntegerField(db_column='ID_MotifConge', primary_key=True)  # Field name made lowercase.
    motif = models.CharField(db_column='Motif', max_length=27, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_MotifConge'


class DimService(models.Model):
    serviceid = models.IntegerField(db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=12)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_Service'


class DimTypeconge(models.Model):
    id_typeconge = models.IntegerField(db_column='ID_TypeConge', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=22, blank=True, null=True)  # Field name made lowercase.
    paye = models.CharField(db_column='Paye', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_TypeConge'


class DimTypecontrat(models.Model):
    typecontratid = models.IntegerField(db_column='TypeContratID', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=31, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_TypeContrat'


class DimTypesalaire(models.Model):
    id_typesalaire = models.IntegerField(db_column='ID_TypeSalaire', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dim_TypeSalaire'


class FactConge(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_employee = models.IntegerField(db_column='ID_Employee')  # Field name made lowercase.
    id_motifconge = models.IntegerField(db_column='ID_MotifConge')  # Field name made lowercase.
    id_typeconge = models.IntegerField(db_column='ID_TypeConge')  # Field name made lowercase.
    id_datedebut = models.IntegerField(db_column='ID_DateDebut')  # Field name made lowercase.
    id_jourdebut = models.IntegerField(db_column='ID_JourDebut')  # Field name made lowercase.
    id_jourfin = models.IntegerField(db_column='ID_JourFin')  # Field name made lowercase.
    nbjourabsent = models.FloatField(db_column='NbJourAbsent', blank=True, null=True)  # Field name made lowercase.
    nbheureservice = models.FloatField(db_column='NbHeureService', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fact_Conge'
        unique_together = (('id', 'id_employee', 'id_motifconge', 'id_typeconge', 'id_datedebut', 'id_jourdebut', 'id_jourfin'),)


class FactSalaire(models.Model):
    id_salaire = models.IntegerField(db_column='ID_Salaire', primary_key=True)  # Field name made lowercase.
    id_employee = models.IntegerField(db_column='ID_Employee')  # Field name made lowercase.
    id_typesalaire = models.IntegerField(db_column='ID_TypeSalaire')  # Field name made lowercase.
    id_modepaiement = models.IntegerField(db_column='ID_ModePaiement')  # Field name made lowercase.
    typecontratid = models.IntegerField(db_column='TypeContratID')  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='ServiceID')  # Field name made lowercase.
    id_fonction = models.IntegerField(db_column='ID_Fonction')  # Field name made lowercase.
    id_etatcivil = models.IntegerField(db_column='ID_EtatCivil')  # Field name made lowercase.
    categorieid = models.IntegerField(db_column='CategorieID')  # Field name made lowercase.
    id_mois = models.IntegerField(db_column='ID_Mois')  # Field name made lowercase.
    noteprime = models.FloatField(db_column='NotePrime', blank=True, null=True)  # Field name made lowercase.
    retenueimpot = models.FloatField(db_column='RetenueImpot', blank=True, null=True)  # Field name made lowercase.
    retenuecnss = models.FloatField(db_column='RetenueCNSS', blank=True, null=True)  # Field name made lowercase.
    retenuetotal = models.FloatField(db_column='RetenueTotal', blank=True, null=True)  # Field name made lowercase.
    primelogement = models.FloatField(db_column='PrimeLogement', blank=True, null=True)  # Field name made lowercase.
    indicevestimentaire = models.FloatField(db_column='IndiceVestimentaire', blank=True, null=True)  # Field name made lowercase.
    primetransport = models.FloatField(db_column='PrimeTransport', blank=True, null=True)  # Field name made lowercase.
    primepresence = models.FloatField(db_column='PrimePresence', blank=True, null=True)  # Field name made lowercase.
    primeresponsabilite = models.FloatField(db_column='PrimeResponsabilite', blank=True, null=True)  # Field name made lowercase.
    primedeplacement = models.FloatField(db_column='PrimeDeplacement', blank=True, null=True)  # Field name made lowercase.
    indemniterisque = models.FloatField(db_column='IndemniteRisque', blank=True, null=True)  # Field name made lowercase.
    primeexceptionnelle = models.FloatField(db_column='PrimeExceptionnelle', blank=True, null=True)  # Field name made lowercase.
    indemnitedifferentielle = models.FloatField(db_column='IndemniteDifferentielle', blank=True, null=True)  # Field name made lowercase.
    primeastreint = models.FloatField(db_column='PrimeAstreint', blank=True, null=True)  # Field name made lowercase.
    primekilometrique = models.FloatField(db_column='PrimeKilometrique', blank=True, null=True)  # Field name made lowercase.
    indemnitepanier = models.FloatField(db_column='IndemnitePanier', blank=True, null=True)  # Field name made lowercase.
    indemnitepanier2 = models.FloatField(db_column='IndemnitePanier2', blank=True, null=True)  # Field name made lowercase.
    indemniteaidkbir = models.FloatField(db_column='IndemniteAidKbir', blank=True, null=True)  # Field name made lowercase.
    rappeltransport = models.FloatField(db_column='RappelTransport', blank=True, null=True)  # Field name made lowercase.
    rappelreclassement = models.FloatField(db_column='RappelReclassement', blank=True, null=True)  # Field name made lowercase.
    primeexceptionnel = models.FloatField(db_column='PrimeExceptionnel', blank=True, null=True)  # Field name made lowercase.
    rappelmoisoctobre = models.FloatField(db_column='RappelMoisOctobre', blank=True, null=True)  # Field name made lowercase.
    primebilan2012 = models.FloatField(db_column='PrimeBilan2012', blank=True, null=True)  # Field name made lowercase.
    correctionindemnite = models.FloatField(db_column='CorrectionIndemnite', blank=True, null=True)  # Field name made lowercase.
    primetotal = models.FloatField(db_column='PrimeTotal', blank=True, null=True)  # Field name made lowercase.
    salairebrut = models.FloatField(db_column='SalaireBrut', blank=True, null=True)  # Field name made lowercase.
    salairenet = models.FloatField(db_column='SalaireNet', blank=True, null=True)  # Field name made lowercase.
    salairenetservi = models.FloatField(db_column='SalaireNetServi', blank=True, null=True)  # Field name made lowercase.
    salaireimposable = models.FloatField(db_column='SalaireImposable', blank=True, null=True)  # Field name made lowercase.
    salairenetrecu = models.FloatField(db_column='SalaireNetRecu', blank=True, null=True)  # Field name made lowercase.
    soldepret = models.FloatField(db_column='SoldePret', blank=True, null=True)  # Field name made lowercase.
    eretenuecnss = models.FloatField(db_column='ERetenueCNSS', blank=True, null=True)  # Field name made lowercase.
    eaccidenttravail = models.FloatField(db_column='EAccidentTravail', blank=True, null=True)  # Field name made lowercase.
    brutsociete = models.FloatField(db_column='BrutSociete', blank=True, null=True)  # Field name made lowercase.
    brutetindemnite = models.FloatField(db_column='BrutEtIndemnite', blank=True, null=True)  # Field name made lowercase.
    brutprime = models.FloatField(db_column='BrutPrime', blank=True, null=True)  # Field name made lowercase.
    brutbilan = models.FloatField(db_column='BrutBilan', blank=True, null=True)  # Field name made lowercase.
    brutprimetotal = models.FloatField(db_column='BrutPrimeTotal', blank=True, null=True)  # Field name made lowercase.
    montantsoldeconge = models.FloatField(db_column='MontantSoldeConge', blank=True, null=True)  # Field name made lowercase.
    assiettecnss = models.FloatField(db_column='AssietteCNSS', blank=True, null=True)  # Field name made lowercase.
    montantassurance = models.FloatField(db_column='MontantAssurance', blank=True, null=True)  # Field name made lowercase.
    retenuepret1 = models.FloatField(db_column='RetenuePret1', blank=True, null=True)  # Field name made lowercase.
    retenuepret2 = models.FloatField(db_column='RetenuePret2', blank=True, null=True)  # Field name made lowercase.
    retenuepret3 = models.FloatField(db_column='RetenuePret3', blank=True, null=True)  # Field name made lowercase.
    retenuepret4 = models.FloatField(db_column='RetenuePret4', blank=True, null=True)  # Field name made lowercase.
    coutparheure = models.FloatField(db_column='CoutParHeure', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fact_Salaire'
        unique_together = (('id_salaire', 'id_employee', 'id_typesalaire', 'id_modepaiement', 'typecontratid', 'serviceid', 'id_fonction', 'id_etatcivil', 'categorieid', 'id_mois'),)
