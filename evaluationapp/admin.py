from django.contrib import admin
from .models import Thematique, Evaluation, Repondant


@admin.register(Thematique)
class ThematiqueAdmin(admin.ModelAdmin):
 list_display = ['titre']


class RepondantInline(admin.StackedInline):
 model = Repondant


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
 list_display = ['titre', 'owner_evalue', 'subject']
 list_filter = ['evalue_nom', 'evalue_prenom']
 search_fields = ['titre', 'commentaire']
 inlines = [RepondantInline]
