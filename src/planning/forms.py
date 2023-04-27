from django.forms import ModelForm
from .models import ENTRAINEMENT
from django import forms

class ENTRAINEMENTForm(ModelForm):
    class Meta:
        model = ENTRAINEMENT
        fields = ['Titre', 'DateEntrainement', 'NomPartie1', 'Partie1', 'TempsPartie1', 'DistancePartie1', 'NomPartie2', 'Partie2', 'TempsPartie2', 'DistancePartie2', 'NomPartie3', 'Partie3', 'TempsPartie3', 'DistancePartie3']
        widgets = {
            'Titre': forms.TextInput(attrs={'class': 'form-control'}),
            'DateEntrainement': forms.DateInput(attrs={'class': 'form-control'}),
            'NomPartie1': forms.TextInput(attrs={'class': 'form-control'}),
            'Partie1': forms.Textarea(attrs={'class': 'form-control'}),
            'TempsPartie1': forms.TimeInput(attrs={'class': 'form-control'}),
            'DistancePartie1': forms.TextInput(attrs={'class': 'form-control'}),
            'NomPartie2': forms.TextInput(attrs={'class': 'form-control'}),
            'Partie2': forms.Textarea(attrs={'class': 'form-control'}),
            'TempsPartie2': forms.TimeInput(attrs={'class': 'form-control'}),
            'DistancePartie2': forms.TextInput(attrs={'class': 'form-control'}),
            'NomPartie3': forms.TextInput(attrs={'class': 'form-control'}),
            'Partie3': forms.Textarea(attrs={'class': 'form-control'}),
            'TempsPartie3': forms.TimeInput(attrs={'class': 'form-control'}),
            'DistancePartie3': forms.TextInput(attrs={'class': 'form-control'}),
        }