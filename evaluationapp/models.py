from django.db import models
from django.contrib.auth.models import User

class Thematique(models.Model):
    titre = models.CharField(max_length=200)
    class Meta:
       ordering = ['titre']
       def __str__(self):
          return self.titre


class Evaluation(models.Model):
    owner_evalue = models.ForeignKey(User,related_name='evalue_created',on_delete=models.CASCADE)
    subject = models.ForeignKey(Thematique,related_name='Evaluations',on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    evalue_nom = models.CharField(max_length=200)
    evalue_prenom = models.CharField(max_length=200)
    evalue_poste= models.CharField(max_length=200)
    evaluateur_nom = models.CharField(max_length=200)
    evaluateur_prenom = models.CharField(max_length=200)
    evaluateur_poste= models.CharField(max_length=200)

    commentaire = models.TextField()


    class Meta:
       ordering = ['titre']
    def __str__(self):
        return self.titre
    
class Repondant(models.Model):
    repondant_type = models.ForeignKey(Evaluation,related_name='repondants',on_delete=models.CASCADE)
    repondant1_nom = models.CharField(max_length=200)
    repondant1_prenom = models.CharField(max_length=200)
    repondant1_mail= models.EmailField(max_length=200)
    repondant2_nom = models.CharField(max_length=200)
    repondant2_prenom = models.CharField(max_length=200)
    repondant2_mail= models.EmailField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ['-created']
    def __str__(self):
        return self.titre




