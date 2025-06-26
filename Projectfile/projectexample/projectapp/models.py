from django.db import models


    
class carlist(models.Model):
    car_name = models.CharField(max_length= 50, default=None)
    model_id = models.IntegerField(default=None)
    cost = models.IntegerField(default=None)
    engine = models.CharField(max_length= 100, default= None)
    time = models.TimeField(default=None)
    
    
    
    
    def __str__(self):
        return self.car_name

# Create your models here.
