# -*- encoding: utf-8 -*-


from django import forms


class QuitterForm(forms.Form):
    age = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Âge",
                "class": "form-control"
            }
        ))
    anciennete = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Ancienneté",
                "class": "form-control"
            }
        ))
    montantrend = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Montant Rend",
                "class": "form-control"
            }
        ))
    salaire = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Salaire Base",
                "class": "form-control"
            }
        ))
    nbrenfant = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Nombre d'enfant",
                "class": "form-control"
            }
        ))
    nbrabsence = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Nombre d'absence",
                "class": "form-control"
            }
        ))
    noteabsence = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Note Absence",
                "class": "form-control"
            }
        ))
    noteassiduite = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Note Assiduité",
                "class": "form-control"
            }
        ))
    dureecontrat = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Durée Contrat",
                "class": "form-control"
            }
        ))
    sexe = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "0 : Homme | 1 : Femme",
                "class": "form-control"
            }
        ))
    titre = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "1 : Cadre | 2 : Maitrise | 3 : Execution",
                "class": "form-control"
            }
        ))
    nbrconge = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Nombre de congés",
                "class": "form-control"
            }
        ))


class NbrCongeForm(forms.Form):
    mois_debut = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Mois",
                "class": "form-control"
            }
        ))
    jour = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Jour",
                "class": "form-control"
            }
        ))

