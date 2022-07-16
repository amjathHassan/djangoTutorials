from django import forms

class CarListCreate(forms.Form):
    car_name = forms.CharField(label= "Car Name", max_length= 100)
    brand_name = forms.CharField(label= "Brand Name", max_length= 100)