from django.urls import path
from django.contrib.auth import views as auth_views
from evaluationapp import views



urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('level1/', views.level1, name='level1'),
    path('level1_02/', views.level1_02, name='level1_02'),
    path('level2/', views.level2, name='level2'),
    path('level3/', views.level3, name='level3'),
    path('talents/', views.talents, name='talents'),
    path('resultats/', views.resultats, name='resultats'),
]
