from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class User1(models.Model):
    area=models.CharField(max_length=50)
    approch=models.IntegerField(max_length=70)
    lead=models.IntegerField(max_length=100)
    
    def __str__(self):
        return str(self.id)
    

