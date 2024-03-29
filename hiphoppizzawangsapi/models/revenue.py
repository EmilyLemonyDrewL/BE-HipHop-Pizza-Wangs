from django.db import models

class Revenue(models.Model):
  total_rev = models.IntegerField()
  
  