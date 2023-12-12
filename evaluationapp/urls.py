from django.urls import path
from django.contrib.auth import views as auth_views
from evaluationapp import views



urlpatterns = [
    path('', views.index, name='index'),
    path('mine/',views.ManageEvaluationListView.as_view(),name='manage_evaluation_list'),
    path('create/',views.EvaluationCreateView.as_view(),name='evaluation_create'),
    path('<pk>/edit/',views.EvaluationUpdateView.as_view(),name='evaluation_edit'),
    path('<pk>/delete/',views.EvaluationDeleteView.as_view(),name='evaluation_delete'),

]