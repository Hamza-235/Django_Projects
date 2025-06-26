from django.test import TestCase
from datetime import datetime
from .models import carlist

class cartest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Carlist = carlist.objects.create(car_name ='ford', model_id ='211', engine='2Lpetrol', cost=233, time =datetime.now())
    
    def testfields(self):
        self.assertIsInstance(self.Carlist.car_name,str)
        self.assertIsInstance(self.Carlist.engine, str)
        self.assertIsInstance(self.Carlist.cost, int)
        
    #def timetest(self):
        self.assertIsInstance(self.Carlist.time, datetime)
        
            
        
        

# Create your tests here.
