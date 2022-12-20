## ✨ Prérequis :
 Python 3.10 +  
 VS Code (IDE)  
 Base de données PostgreSQL nommé : Siame_RH

## ✨ Lancer le Projet : 
   1ére fois :  
   Set-ExecutionPolicy Unrestricted -Scope Process  
   virtualenv env  
   .\env\Scripts\activate  
   pip3 install -r requirements.txt  
   python manage.py makemigrations  
   python manage.py migrate  
   Chaque fois :  
   Set-ExecutionPolicy Unrestricted -Scope Process  
   & "<path_du_projet>/samrise/env/Scripts/Activate.ps1"  
   python manage.py runserver  

## ✨ Si un erreur est déclenché lors de 'python manage.py runserver' sous la forme "Error: No module named nom_module" :   
   pip install nom_module

## ✨ Structure Projet : 

< PROJECT ROOT >  
   |  
   |-- core/                               # Configuration  
   |    |-- settings.py                    # Paramètres Global  
   |    |-- wsgi.py                        # Mode Production  
   |    |-- urls.py                        # URLs définis  
   |
   |-- apps/  
   |    |  
   |    |-- home/                          # Main App  
   |    |    |-- views.py                  # Logique derriére les pages HTML  
   |    |    |-- urls.py                   # Les routes de l'App 'Home'    
   |    |  
   |    |-- authentication/                # Authentification et Inscription  
   |    |    |-- urls.py                   # Les routes de l'authetification  
   |    |    |-- views.py                  # Logique de l'Authentification et Inscription  
   |    |    |-- forms.py                  # Les formulaires d'authetification / inscription  
   |    |  
   |    |-- static/  
   |    |    |-- <css, JS, images>         # Fichiers CSS, Javascripts & Images  
   |    |  
   |    |-- templates/                     # Les fichiers HTML  
   |         |-- includes/                 # Les composants HTML globals  
   |         |    |-- navigation.html      # Barre de navigation Haut  
   |         |    |-- sidebar.html         # Barre de navigation Gauche  
   |         |    |-- footer.html          # App Footer  
   |         |    |-- scripts.html         # Scripts globals  
   |         |  
   |         |-- layouts/                   # Pages HTML Master  
   |         |    |-- base-fullscreen.html  # Utilisé par les pages Authentication  
   |         |    |-- base.html             # Utilisé par les autres pages  
   |         |  
   |         |-- accounts/                  # Pages HTML Authentication  
   |         |    |-- login.html            # Page Login  
   |         |    |-- register.html         # Page Inscription  
   |         |  
   |         |-- home/                      # HTML Pages  
   |              |-- index.html            # Page Index  
   |              |-- 404-page.html         # 404 page  
   |              |-- *.html                # Les autres pages  
   |  
   |-- requirements.txt                     # Modules de Dévelopment - bibliothéques  
   |  
   |-- .env                                 # Environment  
   |-- manage.py                            # Script initial  
   |  
   |-- ************************************************************************  
```

