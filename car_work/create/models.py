from django.db import models

# Create your models here.
class CarListDB(models.Model):
    car_name = models.CharField(max_length= 100)
    brand_name = models.CharField(max_length= 100)

    def __str__(self):
        return f"Car Name : {self.car_name} :: Brand Name : {self.brand_name}"