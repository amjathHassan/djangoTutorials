from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.

class Patients(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    age = models.IntegerField(validators= [MinValueValidator(0), MaxValueValidator(120)])
    heart_rate = models.IntegerField(default = 80, validators= [MinValueValidator(80), MaxValueValidator(120)])

    def __str__(self):
        return f"{self.first_name} {self.last_name} is of age {self.age} heart rate of {self.heart_rate}"

# models.py
class Hotel(models.Model):
	name = models.CharField(max_length=50)
	hotel_Main_Img = models.ImageField(upload_to='images/')
