from django import forms

from . import models


class TalentsChoices(forms.ModelForm):
    class Meta:
        model = models.TalentsModel
        fields = "__all__"
        
    widgets = {
    'created_by': forms.TextInput(attrs={'readonly': 'readonly'}),
    "Le_bosseur" : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    "Activateur" : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Adaptabilité' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Analytique' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Organisateur' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Convaincu' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Commandement' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Communication' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Compétition' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Connexion' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Passé-contexte' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Prudence/Vigilance' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Découvreur_Développeur' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Discipline' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Empathie' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Justesse/Equité' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Focalisation' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Visionaire' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Harmonie' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Idéation' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Intégration' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Individualisation' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Input-Entrée_Information' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Intellection-intellectualisme' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Apprentissage' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Optimiser-maximiser' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Réparer-restaurer' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Positivité' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Relationnel' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Responsabilité' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Confiance_en_soi/résilience' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'différence/originalité' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Sens_stratégique' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),
    'Pouvoir_de_conviction' : forms.CheckboxInput(attrs={'class': "fr-checkbox-group"}),

}

        
class Etape_projet(forms.ModelForm):
    class Meta:
        model = models.etape_projet
        fields = ["contexte", "le_sujet", "realisation", "resultats_obtenus", "suivi",  "points_forts_acquis", "traits_personnalite", "capable_de"]
        widgets ={
            "contexte" : forms.Textarea( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "le_sujet" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "realisation" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "resultats_obtenus" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "suivi" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "points_forts_acquis" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "traits_personnalite" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "capable_de" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),

        }
class Etape_projet2(forms.ModelForm):
    class Meta:
        model = models.etape_projet_02
        fields = ["contexte", "le_sujet", "realisation", "resultats_obtenus", "suivi",  "points_forts_acquis", "traits_personnalite", "capable_de"]
        widgets ={
            "contexte" : forms.Textarea( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "le_sujet" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "realisation" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "resultats_obtenus" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "suivi" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "points_forts_acquis" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "traits_personnalite" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "capable_de" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),

        }

class Etape_forces(forms.ModelForm):
    class Meta:
        model = models.etape_forces
        fields = ["exemple_utilisation", "avis_autres", "utilisation_metier"]
        widgets ={
            "exemple_utilisation" : forms.Textarea( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "avis_autres" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),
            "utilisation_metier" : forms.TextInput( attrs={ 'placeholder': 'Mon texte', 'style': 'width:800px;', 'class': 'fr-input'}),

        }

class Competences(forms.ModelForm):
    class Meta:
        model = models.competences
        fields =["C1_Interagir_oral", "C2_Interagir_ecrit", "C3_Outils_numeriques", "C4_cadres_et_usages",
                 "C5_Gerer_informations", "C6_Organiser_son_activite", "C7_Agir_aleas_situations_urgence", "created_by", "C8_Travail_en_equipe"]
        widgets ={
            'created_by': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
                
        def clean(self):
            super(Competences, self).clean()

            return self.cleaned_data
        
        
        
