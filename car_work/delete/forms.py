from django import forms


class DeleteForm(forms.Form):
    brand_name= forms.CharField(label= "Brand Name", max_length= 100)