# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    #The Data pages
    path('employee', views.employees, name='employee'),
    path('categorie', views.categorie, name='categorie'),
    path('etatcivil', views.etatcivil, name='etatcivil'),
    path('fonction', views.fonction, name='fonction'),
    path('modepaiement', views.modepaiement, name='modepaiement'),
    path('motifconge', views.motifconge, name='motifconge'),
    path('service', views.service, name='service'),
    path('typeconge', views.typeconge, name='typeconge'),
    path('typecontrat', views.typecontrat, name='typecontrat'),
    path('typesalaire', views.typesalaire, name='typesalaire'),
    path('conge', views.conge, name='conge'),
    path('salaire', views.salaire, name='salaire'),
    #Files page
    path('open_categorie_file', views.open_categorie_file, name='open_categorie_file'),
    path('open_conge_file', views.open_conge_file, name='open_conge_file'),
    path('open_etatcivil_file', views.open_etatcivil_file, name='open_etatcivil_file'),
    path('open_fonction_file', views.open_fonction_file, name='open_fonction_file'),
    path('open_historique_file', views.open_historique_file, name='open_historique_file'),
    path('open_modesp_file', views.open_modesp_file, name='open_modesp_file'),
    path('open_motifs_file', views.open_motifs_file, name='open_motifs_file'),
    path('open_personnel_file', views.open_personnel_file, name='open_personnel_file'),
    path('open_salaire_file', views.open_salaire_file, name='open_salaire_file'),
    path('open_service_file', views.open_services_file, name='open_service_file'),
    path('open_tcontrat_file', views.open_tcontrat_file, name='open_tcontrat_file'),
    path('open_tconge_file', views.open_tconge_file, name='open_tconge_file'),
    path('open_tsalaire_file', views.open_tsalaire_file, name='open_tsalaire_file'),
    path('files', views.files, name='files'),
    path('prediction_quitter', views.prediction_quitter, name='prediction_quitter'),
    path('prediction_conge', views.prediction_conge, name='prediction_conge'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
