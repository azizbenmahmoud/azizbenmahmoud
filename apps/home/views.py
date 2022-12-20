# -*- encoding: utf-8 -*-


from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import DimEmployee, DimCategorie, DimEtatcivil, DimFonction, DimModepaiement, DimMotifconge, DimService, DimTypeconge, DimTypecontrat, DimTypesalaire, FactConge, FactSalaire
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pandas as pd
from subprocess import Popen
from .forms import QuitterForm , NbrCongeForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split


@login_required(login_url="/login/")
def employees(request):
    employees_list = DimEmployee.objects.all().order_by('id_employee')
    page = request.GET.get('page', 1)

    paginator = Paginator(employees_list,10)
    
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    return render(request, 'home/employee.html', {'employees':employees})

@login_required(login_url="/login/")
def categorie(request):
    categorie_list = DimCategorie.objects.all().order_by('categorieid')
    page = request.GET.get('page', 1)

    paginator = Paginator(categorie_list,10)
    
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    return render(request, 'home/categories.html', {'categories':categories})

@login_required(login_url="/login/")
def fonction(request):
    fonction_list = DimFonction.objects.all().order_by('id_fonction')
    page = request.GET.get('page', 1)

    paginator = Paginator(fonction_list,10)
    
    try:
        fonctions = paginator.page(page)
    except PageNotAnInteger:
        fonctions = paginator.page(1)
    except EmptyPage:
        fonctions = paginator.page(paginator.num_pages)
    return render(request, 'home/fonction.html', {'fonctions':fonctions})
    
@login_required(login_url="/login/")
def etatcivil(request):
    etatcivil_list = DimEtatcivil.objects.all().order_by('id_etatcivil')
    page = request.GET.get('page', 1)

    paginator = Paginator(etatcivil_list,10)
    
    try:
        etatcivils = paginator.page(page)
    except PageNotAnInteger:
        etatcivils = paginator.page(1)
    except EmptyPage:
        etatcivils = paginator.page(paginator.num_pages)
    return render(request, 'home/etatcivil.html', {'etatcivils':etatcivils})


@login_required(login_url="/login/")
def modepaiement(request):
    modes_list = DimModepaiement.objects.all().order_by('id_modepaiement')
    page = request.GET.get('page', 1)

    paginator = Paginator(modes_list,10)
    
    try:
        modesP = paginator.page(page)
    except PageNotAnInteger:
        modesP = paginator.page(1)
    except EmptyPage:
        modesP = paginator.page(paginator.num_pages)
    return render(request, 'home/modesp.html', {'modesP':modesP})


@login_required(login_url="/login/")
def motifconge(request):
    motifs_list = DimMotifconge.objects.all().order_by('id_motifconge')
    page = request.GET.get('page', 1)

    paginator = Paginator(motifs_list,10)
    
    try:
        motifs = paginator.page(page)
    except PageNotAnInteger:
        motifs = paginator.page(1)
    except EmptyPage:
        motifs = paginator.page(paginator.num_pages)
    return render(request, 'home/motifconge.html', {'motifs':motifs})

@login_required(login_url="/login/")
def service(request):
    services_list = DimService.objects.all().order_by('serviceid')
    page = request.GET.get('page', 1)

    paginator = Paginator(services_list,10)
    
    try:
        services = paginator.page(page)
    except PageNotAnInteger:
        services = paginator.page(1)
    except EmptyPage:
        services = paginator.page(paginator.num_pages)
    return render(request, 'home/service.html', {'services':services})

@login_required(login_url="/login/")
def typeconge(request):
    typesconge_list = DimTypeconge.objects.all().order_by('id_typeconge')
    page = request.GET.get('page', 1)

    paginator = Paginator(typesconge_list,10)
    
    try:
        typesconge = paginator.page(page)
    except PageNotAnInteger:
        typesconge = paginator.page(1)
    except EmptyPage:
        typesconge = paginator.page(paginator.num_pages)
    return render(request, 'home/typeconge.html', {'typesconge':typesconge})

@login_required(login_url="/login/")
def typecontrat(request):
    typescontrat_list = DimTypecontrat.objects.all().order_by('typecontratid')
    page = request.GET.get('page', 1)

    paginator = Paginator(typescontrat_list,10)
    
    try:
        typescontrat = paginator.page(page)
    except PageNotAnInteger:
        typescontrat = paginator.page(1)
    except EmptyPage:
        typescontrat = paginator.page(paginator.num_pages)
    return render(request, 'home/typescontrat.html', {'typescontrat':typescontrat})


@login_required(login_url="/login/")
def typesalaire(request):
    typessalaire_list = DimTypesalaire.objects.all().order_by('id_typesalaire')
    page = request.GET.get('page', 1)

    paginator = Paginator(typessalaire_list,10)
    
    try:
        typessalaire = paginator.page(page)
    except PageNotAnInteger:
        typessalaire = paginator.page(1)
    except EmptyPage:
        typessalaire = paginator.page(paginator.num_pages)
    return render(request, 'home/typesalaire.html', {'typessalaire':typessalaire})


@login_required(login_url="/login/")
def conge(request):
    conges_list = FactConge.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    paginator = Paginator(conges_list,70)
    
    try:
        conges = paginator.page(page)
    except PageNotAnInteger:
        conges = paginator.page(1)
    except EmptyPage:
        conges = paginator.page(paginator.num_pages)
    return render(request, 'home/congés.html', {'conges':conges})

@login_required(login_url="/login/")
def salaire(request):
    salaires_list = FactSalaire.objects.all().order_by('id_salaire')
    page = request.GET.get('page', 1)

    paginator = Paginator(salaires_list,70)
    
    try:
        salaires = paginator.page(page)
    except PageNotAnInteger:
        salaires = paginator.page(1)
    except EmptyPage:
        salaires = paginator.page(paginator.num_pages)
    return render(request, 'home/salaire.html', {'salaires':salaires})


@login_required(login_url="/login/")
def files(request):
    load_files(request)
    return render(request, 'home/datawarehouse_update.html')


@login_required(login_url="/login/")
def prediction_quitter(request):

    form = QuitterForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            age = form.cleaned_data.get("age")
            anciennete = form.cleaned_data.get("anciennete")
            montantrend = form.cleaned_data.get("montantrend")
            salaire = form.cleaned_data.get("salaire")
            nbrenfant = form.cleaned_data.get("nbrenfant")
            nbrabsence = form.cleaned_data.get("nbrabsence")
            noteabsence = form.cleaned_data.get("noteabsence")
            noteassiduite = form.cleaned_data.get("noteassiduite")
            dureecontrat = form.cleaned_data.get("dureecontrat")
            sexe = form.cleaned_data.get("sexe")
            titre = form.cleaned_data.get("titre")
            nbrconge = form.cleaned_data.get("nbrconge")
            res = predict_quitter(age,anciennete,montantrend,salaire,nbrenfant,nbrabsence,noteabsence,noteassiduite,dureecontrat,sexe,titre,nbrconge)
            if res == 0:
                msg = 'Employée va rester'
            else:
                msg = 'Employée va quitter'
        else:
            print(form.errors)
            msg = 'Erreur formulaire'

    return render(request, 'home/prediction_quitter.html', {'form': form, 'msg' : msg})


def predict_quitter(age, anciennete, montantrend, salaire, nbrenfant, nbrabsence, noteabsence, noteassiduite, dureecontrat, sexe, titre, nbrconge):
    input = [age,anciennete,montantrend,salaire,nbrenfant,nbrabsence,noteabsence,noteassiduite,dureecontrat,sexe,titre,nbrconge]
    data = pd.read_csv('D:\\DATA\\AI - ML\\Employees.csv')
    X = data.drop("Quitter", axis=1)
    X = X.drop("ID_Employee", axis=1)
    X = X.drop("Nom", axis=1)
    y = data["Quitter"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
    svm_default = SVC(kernel="rbf", C=10)
    svm_default.fit(X_train, y_train)
    res = svm_default.predict([input])
    print(res[0])
    return res[0]


@login_required(login_url="/login/")
def prediction_conge(request):
    return render(request, 'home/prediction_conges.html')


@login_required(login_url="/login/")
def open_categorie_file(request):
    p = Popen("D:\\DATA\\Data\\Catégorie.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_conge_file(request):
    p = Popen("D:\\DATA\\Data\\Congé.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_etatcivil_file(request):
    p = Popen("D:\\DATA\\Data\\EtatCivil.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_fonction_file(request):
    p = Popen("D:\\DATA\\Data\\Fonction.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_historique_file(request):
    p = Popen("D:\\DATA\\Data\\HistoriqueCongé.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_modesp_file(request):
    p = Popen("D:\\DATA\\Data\\ModePaiement.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_motifs_file(request):
    p = Popen("D:\\DATA\\Data\\MotifCongé.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_personnel_file(request):
    p = Popen("D:\\DATA\\Data\\Personnel.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_salaire_file(request):
    p = Popen("D:\\DATA\\Data\\Salaire_Final.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_services_file(request):
    p = Popen("D:\\DATA\\Data\\Service.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_tcontrat_file(request):
    p = Popen("D:\\DATA\\Data\\TypeContrat.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_tconge_file(request):
    p = Popen("D:\\DATA\\Data\\TypeCongé.csv", shell=True)
    return render(request, 'home/files.html')

@login_required(login_url="/login/")
def open_tsalaire_file(request):
    p = Popen("D:\\DATA\\Data\\TypeSalaire.csv", shell=True)
    return render(request, 'home/files.html')


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

#Executing Files
def load_files(request) :    
    categorie = pd.read_csv("D:\\DATA\\Data\\Catégorie.csv")
    conge = pd.read_csv("D:\\DATA\\Data\\Congé.csv")
    etatcivil = pd.read_csv("D:\\DATA\\Data\\EtatCivil.csv")
    fonction = pd.read_csv("D:\\DATA\\Data\\Fonction.csv")
    historiqueConge = pd.read_csv("D:\\DATA\\Data\\HistoriqueCongé.csv", encoding='latin-1')
    modePaiement = pd.read_csv("D:\\DATA\\Data\\ModePaiement.csv")
    motifConge = pd.read_csv("D:\\DATA\\Data\\MotifCongé.csv")
    personnel = pd.read_csv("D:\\DATA\\Data\\Personnel.csv")
    salaire = pd.read_csv("D:\\DATA\\Data\\Salaire_Final.csv", encoding='latin-1')
    service = pd.read_csv("D:\\DATA\\Data\\Service.csv")
    typeConge = pd.read_csv("D:\\DATA\\Data\\TypeCongé.csv",encoding='latin-1')
    typeContrat = pd.read_csv("D:\\DATA\\Data\\TypeContrat.csv",encoding='latin-1')
    typeSalaire = pd.read_csv("D:\\DATA\\Data\\TypeSalaire.csv")

    #Data Cleaning
    #Supprimer les colonnes vides
    categorie_vides = [col for col in categorie.columns if categorie[col].isnull().all()]
    categorie.drop(categorie_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    conge_vides = [col for col in conge.columns if conge[col].isnull().all()]
    conge.drop(conge_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    etatcivil_vides = [col for col in etatcivil.columns if etatcivil[col].isnull().all()]
    etatcivil.drop(etatcivil_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    fonction_vides = [col for col in fonction.columns if fonction[col].isnull().all()]
    fonction.drop(fonction_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    historiqueConge_vides = [col for col in historiqueConge.columns if historiqueConge[col].isnull().all()]
    historiqueConge.drop(historiqueConge_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    modePaiement_vides = [col for col in modePaiement.columns if modePaiement[col].isnull().all()]
    modePaiement.drop(modePaiement_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    motifConge_vides = [col for col in motifConge.columns if motifConge[col].isnull().all()]
    motifConge.drop(motifConge_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    personnel_vides = [col for col in personnel.columns if personnel[col].isnull().all()]
    personnel.drop(personnel_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    salaire_vides = [col for col in salaire.columns if salaire[col].isnull().all()]
    salaire.drop(salaire_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    service_vides = [col for col in service.columns if service[col].isnull().all()]
    service.drop(service_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    typeConge_vides = [col for col in typeConge.columns if typeConge[col].isnull().all()]
    typeConge.drop(typeConge_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    typeContrat_vides = [col for col in typeContrat.columns if typeContrat[col].isnull().all()]
    typeContrat.drop(typeContrat_vides,
        axis=1,
        inplace=True)
    #Supprimer les colonnes vides
    typeSalaire_vides = [col for col in typeSalaire.columns if typeSalaire[col].isnull().all()]
    typeSalaire.drop(typeSalaire_vides,
        axis=1,
        inplace=True)


    for col in categorie.columns :
        if(categorie[col].dtype == "float64") : categorie[col].fillna(0,inplace=True)
        if(categorie[col].dtype == "int64") : categorie[col].fillna(0,inplace=True)
        if(categorie[col].dtype == "object") : categorie[col].fillna("Non specifie",inplace=True)

    for col in conge.columns :
        if(conge[col].dtype == "float64") : conge[col].fillna(0,inplace=True)
        if(conge[col].dtype == "int64") : conge[col].fillna(0,inplace=True)
        if(conge[col].name == "DateDebut_D_4") : conge[col].fillna("1/1/2026",inplace=True)
        if(conge[col].dtype == "object") : conge[col].fillna("Non specifie",inplace=True)

    for col in etatcivil.columns :
        if(etatcivil[col].dtype == "float64") : etatcivil[col].fillna(0,inplace=True)
        if(etatcivil[col].dtype == "int64") : etatcivil[col].fillna(0,inplace=True)
        if(etatcivil[col].dtype == "object") : etatcivil[col].fillna("Non specifie",inplace=True)

    for col in fonction.columns :
        if(fonction[col].dtype == "float64") : fonction[col].fillna(0,inplace=True)
        if(fonction[col].dtype == "int64") : fonction[col].fillna(0,inplace=True)
        if(fonction[col].dtype == "object") : fonction[col].fillna("Non specifie",inplace=True)

    for col in historiqueConge.columns :
        if(historiqueConge[col].dtype == "float64") : historiqueConge[col].fillna(0,inplace=True)
        if(historiqueConge[col].dtype == "int64") : historiqueConge[col].fillna(0,inplace=True)
        if(historiqueConge[col].dtype == "object") : historiqueConge[col].fillna("Non specifie",inplace=True)

    for col in modePaiement.columns :
        if(modePaiement[col].dtype == "float64") : modePaiement[col].fillna(0,inplace=True)
        if(modePaiement[col].dtype == "int64") : modePaiement[col].fillna(0,inplace=True)
        if(modePaiement[col].dtype == "object") : modePaiement[col].fillna("Non specifie",inplace=True)

    for col in motifConge.columns :
        if(motifConge[col].dtype == "float64") : motifConge[col].fillna(0,inplace=True)
        if(motifConge[col].dtype == "int64") : motifConge[col].fillna(0,inplace=True)
        if(motifConge[col].dtype == "object") : motifConge[col].fillna("Non specifie",inplace=True)

    for col in personnel.columns :
        if(personnel[col].dtype == "float64") : personnel[col].fillna(0,inplace=True)
        if(personnel[col].dtype == "int64") : personnel[col].fillna(0,inplace=True)
        if(personnel[col].dtype == "object") : personnel[col].fillna("Non specifie",inplace=True)

    for col in salaire.columns :
        if(salaire[col].name == "TypeSalaire") : salaire[col].fillna(99,inplace=True)
        if(salaire[col].dtype == "float64") : salaire[col].fillna(0,inplace=True)
        if(salaire[col].dtype == "int64") : salaire[col].fillna(0,inplace=True)
        if(salaire[col].dtype == "object") : salaire[col].fillna("Non specifie",inplace=True)

    for col in service.columns :
        if(service[col].dtype == "float64") : service[col].fillna(0,inplace=True)
        if(service[col].dtype == "int64") : service[col].fillna(0,inplace=True)
        if(service[col].dtype == "object") : service[col].fillna("Non specifie",inplace=True)

    for col in typeConge.columns :
        if(typeConge[col].dtype == "float64") : typeConge[col].fillna(0,inplace=True)
        if(typeConge[col].dtype == "int64") : typeConge[col].fillna(0,inplace=True)
        if(typeConge[col].dtype == "object") : typeConge[col].fillna("Non specifie",inplace=True)

    for col in typeContrat.columns :
        if(typeContrat[col].dtype == "float64") : typeContrat[col].fillna(0,inplace=True)
        if(typeContrat[col].dtype == "int64") : typeContrat[col].fillna(0,inplace=True)
        if(typeContrat[col].dtype == "object") : typeContrat[col].fillna("Non specifie",inplace=True)

    for col in typeSalaire.columns :
        if(typeSalaire[col].dtype == "float64") : typeSalaire[col].fillna(0,inplace=True)
        if(typeSalaire[col].dtype == "int64") : typeSalaire[col].fillna(0,inplace=True)
        if(typeSalaire[col].dtype == "object") : typeSalaire[col].fillna("Non specifie",inplace=True)

    #Inserting to Database

    from sqlalchemy import create_engine
    engine = create_engine('postgresql://postgres:0903@localhost:5432/Siame_SA')


    categorie.to_sql('Categorie', engine, index=False,if_exists='replace')
    print("Categorie Done ..")
    conge.to_sql('Conge', engine, index=False,if_exists='replace')
    print("Conge Done ..")
    etatcivil.to_sql('EtatCivil', engine, index=False,if_exists='replace')
    print("EtatCivil Done ..")
    fonction.to_sql('Fonction', engine, index=False,if_exists='replace')
    print("Fonction Done ..")
    historiqueConge.to_sql('HistoriqueConge', engine, index=False,if_exists='replace')
    print("HistoriqueConge Done ..")
    modePaiement.to_sql('ModePaiement', engine, index=False,if_exists='replace')
    print("ModePaiement Done ..")
    motifConge.to_sql('MotifConge', engine, index=False,if_exists='replace')
    print("MotifConge Done ..")
    personnel.to_sql('Employee', engine, index=False,if_exists='replace')
    print("Employee Done ..")
    salaire.to_sql('Salaire', engine, index=False,if_exists='replace')
    print("Salaire Done ..")
    service.to_sql('Service', engine, index=False,if_exists='replace')
    print("Service Done ..")
    typeConge.to_sql('TypeConge', engine, index=False,if_exists='replace')
    print("TypeConge Done ..")
    typeContrat.to_sql('TypeContrat', engine, index=False,if_exists='replace')
    print("TypeContrat Done ..")
    typeSalaire.to_sql('TypeSalaire', engine, index=False,if_exists='replace')
    print("TypeSalaire Done ..")


    #'{os.path.join(os.path.dirname(__file__),
    import subprocess
    subprocess.call([r'D:\\DATA\\ETL\\ETL_Categorie_0.1\\ETL_Categorie\\ETL_Categorie_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_Employee_0.1\\ETL_Employee\\ETL_Employee_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_EtatCivil_0.1\\ETL_EtatCivil\\ETL_EtatCivil_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_Fonction_0.1\\ETL_Fonction\\ETL_Fonction_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_ModePaiement_0.1\\ETL_ModePaiement\\ETL_ModePaiement_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_MotifConge_0.1\\ETL_MotifConge\\ETL_MotifConge_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_Service_0.1\\ETL_Service\\ETL_Service_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_TypeConge_0.1\\ETL_TypeConge\\ETL_TypeConge_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_TypeContrat_0.1\\ETL_TypeContrat\\ETL_TypeContrat_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_TypeSalaire_0.1\\ETL_TypeSalaire\\ETL_TypeSalaire_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_Fact_Conge_0.1\\ETL_Fact_Conge\\ETL_Fact_Conge_run.bat'])
    subprocess.call([r'D:\\DATA\\ETL\\ETL_Fact_Salaire_0.1\\ETL_Fact_Salaire\\ETL_Fact_Salaire_run.bat'])
