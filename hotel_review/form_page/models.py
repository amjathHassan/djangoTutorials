from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class SignUpFormDB(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    email = models.EmailField()

    def __str__(self):
        return f"first name : {self.first_name} last name : {self.last_name} email : {self.email}"

class ModelFormDB(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    age = models.IntegerField(validators= [MinValueValidator(0), MaxValueValidator(120)])

    def __str__(self):
        return f"first name : {self.first_name} last name : {self.last_name} age : {self.age}"