from django.db import models
from django.forms import CharField
from multiselectfield import MultiSelectField


from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField


CHOICES_TALENTS = (('Le_bosseur','Le_bosseur'),
('Activateur','Activateur'),
('Adaptabilité',' Adaptabilité'),
('Analytique','Analytique'),
('Organisateur','Organisateur'),
('Convaincu','Convaincu'),
('Commandement','Commandement'),
('Communication','Communication'),
('Compétition','Compétition'),
('Connexion','Connexion'),
('Passé-contexte','Passé-contexte'),
('Prudence/Vigilance','Prudence/Vigilance'),
('Découvreur_Développeur','Découvreur_Développeur'),
('Discipline','Discipline'),
('Empathie','Empathie'),
('Justesse/Equité','Justesse/Equité'),
('Focalisation','Focalisation'),
('Visionaire','Visionaire'),
('Harmonie','Harmonie'),
('Idéation','Idéation'),
('Intégration','Intégration'),
('Individualisation','Individualisation'),
('Input-Entrée_Information','Input-Entrée_Information'),
('Intellection-intellectualisme','Intellection-intellectualisme'),
('Apprentissage','Apprentissage'),
('Optimiser-maximiser','Optimiser-maximiser'),
('Réparer-restaurer','Réparer-restaurer'),
('Positivité','Positivité'),
('Relationnel','Relationnel'),
('Responsabilité','Responsabilité'),
('Confiance_en_soi/résilience','Confiance_en_soi/résilience'),
('Différence/originalité','Différence/originalité'),
('Sens_stratégique','Sens_stratégique'),
('Pouvoir_de_conviction','Pouvoir_de_conviction'),

)



class TalentsModel(models.Model):

    created_by = CurrentUserField()
    talents_liste = MultiSelectField(choices=CHOICES_TALENTS,  max_choices=5, max_length=200)

class etape_projet(models.Model):

    created_by = CurrentUserField()

    contexte = models.CharField(max_length=1000, default="")
    le_sujet = models.CharField(max_length=1000, default="")
    realisation = models.CharField(max_length=1000, default="")
    resultats_obtenus = models.CharField(max_length=1000, default="")
    suivi = models.CharField(max_length=1000, default="")
    points_forts_acquis = models.CharField(max_length=1000, default="")
    traits_personnalité = models.CharField(max_length=1000, default="")
    capable_de = models.CharField(max_length=1000, default="")

class etape_projet_02(models.Model):

    created_by = CurrentUserField()

    contexte = models.CharField(max_length=1000, default="")
    le_sujet = models.CharField(max_length=1000, default="")
    realisation = models.CharField(max_length=1000, default="")
    resultats_obtenus = models.CharField(max_length=1000, default="")
    suivi = models.CharField(max_length=1000, default="")
    points_forts_acquis = models.CharField(max_length=1000, default="")
    traits_personnalité = models.CharField(max_length=1000, default="")
    capable_de = models.CharField(max_length=1000, default="")

class etape_forces(models.Model):

    created_by = CurrentUserField()
    exemple_utilisation = models.CharField(max_length=1000, default="")
    avis_autres = models.CharField(max_length=1000, default="")
    utilisation_metier = models.CharField(max_length=1000, default="")

class competences(models.Model):

    created_by = CurrentUserField()
    palier_1 = "palier_1"
    palier_2 = "palier_2"
    palier_3 = "palier_3"
    palier_4 = "palier_4"
    palier_5 = "palier_5"
    palier_6 = "palier_6"
    C1_CHOICES = {
        (palier_1 , "Présente et décrit partiellement son parcours et son activité"),
        (palier_2 , "Interagit avec des éléments familiers et dans le temps"),
        (palier_3 , "Explique et justifie son choix auprès d'interlocuteurs variés"),
        (palier_4 , "Adapte ses manières de dire/ne pas dire en fonction des situations de communication"),
        (palier_5 , "Augment et facilite l'élaboration de points de vue au sein de collectifs connus."),
        (palier_6 , "Varie ses manières de communiquer en fonction des publics et des enjeux liés à toute situation institutionnelle"),

    }

    palier_1 = "palier_1"
    palier_2 = "palier_2"
    palier_3 = "palier_3"
    palier_4 = "palier_4"
    palier_5 = "palier_5"
    palier_6 = "palier_6"
    C2_CHOICES = {
        (palier_1, "Identifier les éléments clés d'un écrit"),
        (palier_2, "Identifier des informations pertinants dans des textes"),
        (palier_3, "Utilise la plupart des écrits nécessaire à son activité"),
        (palier_4, "Traite et produit des textes pour son activité courante et à usage interne"),
        (palier_5, "Analyse des écrits techniques"),
        (palier_6, "Gere, traite et produit des textes complexes et variés"),

    }
    palier_1 = "palier_1"
    palier_2 = "palier_2"
    palier_3 = "palier_3"
    palier_4 = "palier_4"
    palier_5 = "palier_5"
    palier_6 = "palier_6"
    C3_CHOICES = {
        (palier_1, "Réalise des tâches élémentaires avec un outil connu"),
        (palier_2, "Utilise des fonctions de base de quelques outils numériques"),
        (palier_3, "Utilise régulièrement des outils numériques"),
        (palier_4, "Personnalise les ressources numériques au service de son activité"),
        (palier_5, "Elabore des supports variés et complexes"),
        (palier_6, "Produit des contenus multimédia à l'aide de plateformes"),
    }

    palier_1 = "palier_1"
    palier_2 = "palier_2"
    palier_3 = "palier_3"
    palier_4 = "palier_4"
    palier_5 = "palier_5"
    palier_6 = "palier_6"
    C4_CHOICES = {
        (palier_1, "Identifier les cadres réglementaires de son activité"),
        (palier_2, "Applique les procédures et les codes relationnels en usage"),
        (palier_3, "Met en oeuvre les consignes et procédures"),
        (palier_4, "Assure le contrôle le respect des cadres et usages"),
        (palier_5, "Assure le respect des cadres et usages"),
        (palier_6, "Adapte si nécessaire les règles de fonctionnement liées aux cadres et usages"),
    }

    palier_1 = "palier_1"
    palier_2 = "palier_2"
    palier_3 = "palier_3"
    palier_4 = "palier_4"
    palier_5 = "palier_5"
    palier_6 = "palier_6"
    C5_CHOICES = {
        (palier_1, "Identifier les informations misent à disposition pour son activité"),
        (palier_2, "Vérifie la disponibilité des informations nécessaires à son activité"),
        (palier_3, "Sélectionne des informations en fonction des objectifs et des circonstances de l'activité"),
        (palier_4, "Evalue la pertinence de l'information et la diffuse"),
        (palier_5, "Produit pour autrui de l'information en vue d'aider à la décision"),
        (palier_6, "Interpréter des informations pour prendre des décisions"),
    }

    palier_1 = "palier_1"
    palier_2 = "palier_2"
    palier_3 = "palier_3"
    palier_4 = "palier_4"
    palier_5 = "palier_5"
    palier_6 = "palier_6"
    C6_CHOICES = {
        (palier_1, "Identifier les éléments structurants l'organisation de l'activité prévue"),
        (palier_2, "Applique l'organisation prévue pour l'activité"),
        (palier_3, "Organise son activité au regard des exigenses d'une situation"),
        (palier_4, "Ajuste si nécessaire l'organisatin de son activité et/ou celle de son équipe"),
        (palier_5, "Définit l'organisation adéquate au regard des paramètres des projets"),
        (palier_6, "Elabore et coordonne l'organisation de plusieurs services"),
    }

    palier_1 = "palier_1"
    palier_2 = "palier_2"
    palier_3 = "palier_3"
    palier_4 = "palier_4"
    palier_5 = "palier_5"
    palier_6 = "palier_6"
    C7_CHOICES = {
        (palier_1, "Identifier un évènement imprévu"),
        (palier_2, "Proposer une action adaptée à sa hiérarchie face à un évènement imprévu"),
        (palier_3, "Met en oeuvre une action adpatée face à évènement imprévu en situation courante"),
        (palier_4, "Agit après consultation de sa hiérarchie face à des évènements exceptionnels"),
        (palier_5, "Propose des solutions adaptées en situation exceptionnelle"),
        (palier_6, "Tranche des solutions proposées"),
    }

    palier_1 = "palier_1"
    palier_2 = "palier_2"
    palier_3 = "palier_3"
    palier_4 = "palier_4"
    palier_5 = "palier_5"
    palier_6 = "palier_6"
    C8_CHOICES = {
        (palier_1, "Se conforme aux modes de fonctionnement d'une équipe donnée"),
        (palier_2, "Identifie le rôle des participants et sa position dans le groupe"),
        (palier_3, "Fait des propositions et prend en compte les avis des membres de l'équipe"),
        (palier_4, "Anime le travail collectif, peut varier sa place et son rôle"),
        (palier_5, "Met en place un fonctionnement pour développer le travail de son équipe"),
        (palier_6, "Assure la coopération entre équipes et distribu les rôles"),
    }



    C1_Interagir_oral = models.CharField(max_length=20, choices =  C1_CHOICES, default = palier_1)
    C2_Interagir_écrit = models.CharField(max_length=20, choices =  C2_CHOICES, default = palier_1)
    C3_Outils_numériques = models.CharField(max_length=20, choices =  C3_CHOICES, default = palier_1)
    C4_cadres_et_usages = models.CharField(max_length=20, choices =  C4_CHOICES, default = palier_1)
    C5_Gérer_informations = models.CharField(max_length=20, choices =  C5_CHOICES, default = palier_1)
    C6_Organiser_son_activité = models.CharField(max_length=20, choices =  C6_CHOICES, default = palier_1)
    C7_Agir_aléas_situations_urgence = models.CharField(max_length=20, choices =  C7_CHOICES, default = palier_1)
    C8_Travail_en_équipe = models.CharField(max_length=20, choices =  C8_CHOICES, default = palier_1)
    




