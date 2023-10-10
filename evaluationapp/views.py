from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import plotly.express as px
import numpy as np


from evaluationapp.models import TalentsModel, competences, etape_forces, etape_projet, etape_projet_02
from .forms import Competences, Etape_forces, Etape_projet, Etape_projet2, TalentsChoices
from django.contrib.auth.decorators import login_required
    
def index(request):
     return render(request, 'home.html')


@login_required 
def dashboard(request):
     return render(request, 'dashboard.html')


@login_required 
def level1(request):
     if request.method == 'POST':
          form_etape = Etape_projet(request.POST)
          if form_etape.is_valid():
               form_etape.save()
               result_01 = etape_projet.objects.all().order_by('-id').values()[:1]
               context={}
               context['form_etape']= Etape_projet
               context['talent_form']= TalentsChoices
               context['last_form']= Etape_forces
               context['resultats']= result_01
               
               return render(request, 'resultats01.html', context)
          else :
               return HttpResponse('Les données utilisateur ne sont pas conformes')
     
     else:
          context={}
          context['form_etape']= Etape_projet
          return render(request, 'level1.html', context)
     
@login_required 
def level1_02(request):
     if request.method == 'POST':
          form_etape_02 = Etape_projet2(request.POST)
          if form_etape_02.is_valid():
               form_etape_02.save()
               result_01 = etape_projet.objects.all().order_by('-id').values()[:1]
               result_02 = etape_projet_02.objects.all().order_by('-id').values()[:1]
             
               context={}
               context['form_etape_02']= Etape_projet2
               context['talent_form']= TalentsChoices
               context['last_form']= Etape_forces
               context['resultats']= result_01
               context['resultats_02']= result_02
               
               return render(request, 'resultats01_02.html', context)
          else :
               return HttpResponse('Les données utilisateur ne sont pas conformes')
     
     else:
          context={}
          context['form_etape_02']= Etape_projet2
          return render(request, 'level1_02.html', context)


@login_required 
def level2(request):
     if request.method == 'POST':
          talent_form = TalentsChoices(request.POST)
          last_form = Etape_forces(request.POST)
          if request.method == 'POST' and 'bouton01' in request.POST:
               if  talent_form.is_valid():
                    talent_form.save()
                    context={}
                    context['text_etape'] = "Vous pouvez passer à l'étape suivante"
                    context['talent_form']= TalentsChoices()
                    context['last_form']= Etape_forces()
                    result_talents = TalentsModel.objects.all().order_by('-id').values()[:1]
                    result_use = result_talents.values_list('talents_liste')
                   
                    print(result_use)
               
                    context['talent_01']= result_talents
               return render(request, 'level2.html', context)
          if request.method == 'POST' and 'bouton02' in request.POST:
               if  last_form.is_valid():
                    last_form.save()
                    result_01 = etape_projet.objects.all().order_by('-id').values()[:1]
                    result_talents = TalentsModel.objects.all().order_by('-id').values()[:1]
                    result_last = etape_forces.objects.all().order_by('-id').values()[:1]
                    list_talents = result_talents.to_dataframe()
                    context={}
                    context['talent_form']= TalentsChoices()
                    context['last_form']= Etape_forces()
                    context['resultats']= result_01
                    context['result_last']= result_last
                    context['result_talents']= result_talents
                 

               return render(request, 'resultats02.html', context)
     else:
          context={}
          context['talent_form']= TalentsChoices()
          context['last_form']= Etape_forces()
          return render(request, 'level2.html', context)



     
@login_required 
def level3(request):
     if request.method == 'POST':
          details= Competences(request.POST)
          if details.is_valid():
               competences_post = details.save(commit=False)
               competences_post.save()
               form_comp = Competences()
               result_01 = etape_projet.objects.all().values().order_by('-id').values()[:1]
               result_talents = TalentsModel.objects.all().order_by('-id').values()[:1]
               result_last = etape_forces.objects.all().order_by('-id').values()[:1]
               result_competences = competences.objects.all().order_by('-id').values()[:1]
               context={}
               context['talent_form']= TalentsChoices()
               context['last_form']= Etape_forces()
               context['resultats']= result_01
               context['result_last']= result_last
               context['result_talents']= result_talents
               context['result_competences']= result_competences
               context['form_comp']= form_comp

               #########chart code ##########
               df_result=pd.DataFrame(result_competences)
               df_result = df_result.drop(columns=['id', 'created_by_id'])
               
               df_result=df_result.replace(["palier_1", "palier_2", "palier_3", "palier_4", "palier_5", "palier_6", "palier_7", "palier_8"], [1, 2, 3, 4, 5, 6, 7, 8])
               r=df_result.iloc[0]
               fig_competences= px.line_polar(df_result,r=r, theta=["C1_Interagir_oral", "C2_Interagir_écrit", "C3_Outils_numériques", "C4_cadres_et_usages",
                 "C5_Gérer_informations", "C6_Organiser_son_activité", "C7_Agir_aléas_situations_urgence", "C8_Travail_en_équipe"], line_close=True)
               fig_competences.update_traces(fill='toself')
               chart_competences= fig_competences.to_html()
               context['chart_competences']= chart_competences
     
               return render(request, 'resultats03.html', context)
          else :
               return HttpResponse('Les données utilisateur ne sont pas conformes')
     
     else:
          form_comp = Competences(None)
          return render(request, 'level3.html', {'form_comp': form_comp})
     return render(request, 'level3.html')

@login_required 
def resultats(request):
      result_01 = etape_projet.objects.all().values()
      result_talents = TalentsModel.objects.all().values()
      result_last = etape_forces.objects.all().values()
      result_competences = competences.objects.all().values()
      context={}
      context['resultats']= result_01
      context['result_talents']= result_talents
      context['result_last']= result_last
      context['result_competences']= result_competences

      return render(request, 'resultats02.html', context)


@login_required 
def talents(request):
     form =TalentsChoices(request.POST)
     if form.is_valid():
            form.save()
     context={}
     context['form']= TalentsChoices()
     return render(request, 'talentPage.html', context)