# Generated by Django 3.2.18 on 2023-10-10 08:09

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('evaluationapp', '0006_auto_20231009_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competences',
            name='C1_Interagir_oral',
            field=models.CharField(choices=[('palier_5', "Augment et facilite l'élaboration de points de vue au sein de collectifs connus."), ('palier_1', 'Présente et décrit partiellement son parcours et son activité'), ('palier_2', 'Interagit avec des éléments familiers et dans le temps'), ('palier_4', 'Adapte ses manières de dire/ne pas dire en fonction des situations de communication'), ('palier_3', "Explique et justifie son choix auprès d'interlocuteurs variés"), ('palier_6', 'Varie ses manières de communiquer en fonction des publics et des enjeux liés à toute situation institutionnelle')], default='palier_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='competences',
            name='C2_Interagir_écrit',
            field=models.CharField(choices=[('palier_3', 'Utilise la plupart des écrits nécessaire à son activité'), ('palier_6', 'Gere, traite et produit des textes complexes et variés'), ('palier_1', "Identifier les éléments clés d'un écrit"), ('palier_4', 'Traite et produit des textes pour son activité courante et à usage interne'), ('palier_2', 'Identifier des informations pertinants dans des textes'), ('palier_5', 'Analyse des écrits techniques')], default='palier_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='competences',
            name='C3_Outils_numériques',
            field=models.CharField(choices=[('palier_6', "Produit des contenus multimédia à l'aide de plateformes"), ('palier_5', 'Elabore des supports variés et complexes'), ('palier_3', 'Utilise régulièrement des outils numériques'), ('palier_4', 'Personnalise les ressources numériques au service de son activité'), ('palier_1', 'Réalise des tâches élémentaires avec un outil connu'), ('palier_2', 'Utilise des fonctions de base de quelques outils numériques')], default='palier_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='competences',
            name='C4_cadres_et_usages',
            field=models.CharField(choices=[('palier_2', 'Applique les procédures et les codes relationnels en usage'), ('palier_4', 'Assure le contrôle le respect des cadres et usages'), ('palier_6', 'Adapte si nécessaire les règles de fonctionnement liées aux cadres et usages'), ('palier_3', 'Met en oeuvre les consignes et procédures'), ('palier_1', 'Identifier les cadres réglementaires de son activité'), ('palier_5', 'Assure le respect des cadres et usages')], default='palier_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='competences',
            name='C5_Gérer_informations',
            field=models.CharField(choices=[('palier_3', "Sélectionne des informations en fonction des objectifs et des circonstances de l'activité"), ('palier_1', 'Identifier les informations misent à disposition pour son activité'), ('palier_4', "Evalue la pertinence de l'information et la diffuse"), ('palier_5', "Produit pour autrui de l'information en vue d'aider à la décision"), ('palier_6', 'Interpréter des informations pour prendre des décisions'), ('palier_2', 'Vérifie la disponibilité des informations nécessaires à son activité')], default='palier_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='competences',
            name='C6_Organiser_son_activité',
            field=models.CharField(choices=[('palier_4', "Ajuste si nécessaire l'organisatin de son activité et/ou celle de son équipe"), ('palier_1', "Identifier les éléments structurants l'organisation de l'activité prévue"), ('palier_3', "Organise son activité au regard des exigenses d'une situation"), ('palier_2', "Applique l'organisation prévue pour l'activité"), ('palier_5', "Définit l'organisation adéquate au regard des paramètres des projets"), ('palier_6', "Elabore et coordonne l'organisation de plusieurs services")], default='palier_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='competences',
            name='C7_Agir_aléas_situations_urgence',
            field=models.CharField(choices=[('palier_6', 'Tranche des solutions proposées'), ('palier_4', 'Agit après consultation de sa hiérarchie face à des évènements exceptionnels'), ('palier_3', 'Met en oeuvre une action adpatée face à évènement imprévu en situation courante'), ('palier_2', 'Proposer une action adaptée à sa hiérarchie face à un évènement imprévu'), ('palier_1', 'Identifier un évènement imprévu'), ('palier_5', 'Propose des solutions adaptées en situation exceptionnelle')], default='palier_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='competences',
            name='C8_Travail_en_équipe',
            field=models.CharField(choices=[('palier_5', 'Met en place un fonctionnement pour développer le travail de son équipe'), ('palier_2', 'Identifie le rôle des participants et sa position dans le groupe'), ('palier_3', "Fait des propositions et prend en compte les avis des membres de l'équipe"), ('palier_6', 'Assure la coopération entre équipes et distribu les rôles'), ('palier_1', "Se conforme aux modes de fonctionnement d'une équipe donnée"), ('palier_4', 'Anime le travail collectif, peut varier sa place et son rôle')], default='palier_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='talentsmodel',
            name='talents_liste',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Le_bosseur', 'Le_bosseur'), ('Activateur', 'Activateur'), ('Adaptabilité', ' Adaptabilité'), ('Analytique', 'Analytique'), ('Organisateur', 'Organisateur'), ('Convaincu', 'Convaincu'), ('Commandement', 'Commandement'), ('Communication', 'Communication'), ('Compétition', 'Compétition'), ('Connexion', 'Connexion'), ('Passé-contexte', 'Passé-contexte'), ('Prudence/Vigilance', 'Prudence/Vigilance'), ('Découvreur_Développeur', 'Découvreur_Développeur'), ('Discipline', 'Discipline'), ('Empathie', 'Empathie'), ('Justesse/Equité', 'Justesse/Equité'), ('Focalisation', 'Focalisation'), ('Visionaire', 'Visionaire'), ('Harmonie', 'Harmonie'), ('Idéation', 'Idéation'), ('Intégration', 'Intégration'), ('Individualisation', 'Individualisation'), ('Input-Entrée_Information', 'Input-Entrée_Information'), ('Intellection-intellectualisme', 'Intellection-intellectualisme'), ('Apprentissage', 'Apprentissage'), ('Optimiser-maximiser', 'Optimiser-maximiser'), ('Réparer-restaurer', 'Réparer-restaurer'), ('Positivité', 'Positivité'), ('Relationnel', 'Relationnel'), ('Responsabilité', 'Responsabilité'), ('Confiance_en_soi/résilience', 'Confiance_en_soi/résilience'), ('Différence/originalité', 'Différence/originalité'), ('Sens_stratégique', 'Sens_stratégique'), ('Pouvoir_de_conviction', 'Pouvoir_de_conviction')], max_length=200),
        ),
    ]