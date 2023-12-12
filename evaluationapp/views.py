from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Evaluation

    
def index(request):
     return render(request, 'index.html')


class ManageEvaluationListView(ListView):
   model = Evaluation
   template_name = 'evaluations/manage/evaluation/list.html'
   def get_queryset(self):
      qs = super().get_queryset()
      return qs.filter(owner_evalue=self.request.user)
   
class OwnerMixin(object):
 def get_queryset(self):
   qs = super().get_queryset()
   return qs.filter(owner_evalue=self.request.user)
 
class OwnerEditMixin(object):
  def form_valid(self, form):
    form.instance.owner_evalue = self.request.user
    return super().form_valid(form)
  
class OwnerEvaluationMixin(OwnerMixin, LoginRequiredMixin,PermissionRequiredMixin):
 model = Evaluation
 fields = ['subject', 'titre','evalue_nom', 'evalue_prenom', 'evalue_poste', 'evaluateur_nom', 'evaluateur_prenom', 'evaluateur_poste']
 success_url = reverse_lazy('manage_evaluation_list')
 
class OwnerEvaluationEditMixin(OwnerEvaluationMixin, OwnerEditMixin):
  template_name = 'evaluations/manage/evaluation/form.html'

class ManageEvaluationListView(OwnerEvaluationMixin, ListView):
 template_name = 'evaluations/manage/evaluation/list.html'
 permission_required = 'evaluations.view_evaluation'


class EvaluationCreateView(OwnerEvaluationEditMixin, CreateView):
  permission_required = 'evaluations.add_evaluation'

class EvaluationUpdateView(OwnerEvaluationEditMixin, UpdateView):
  permission_required = 'evaluations.change_evaluation'

class EvaluationDeleteView(OwnerEvaluationMixin, DeleteView):
 template_name = 'evaluations/manage/evaluation/delete.html'
 permission_required = 'evaluations.delete_evaluation'