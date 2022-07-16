from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label= "First Name", max_length= 100)
    last_name = forms.CharField(label= "Last Name", max_length= 100)
    email = forms.EmailField()
    pass



# forms.py
from .models import *
  
class HotelForm(forms.ModelForm):
  
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']











# from django import forms

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label = "First Name", max_length= 100)
#     last_name = forms.CharField(label = "Last Name", max_length= 100)
#     email = forms.EmailField(label= 'Email')
#     review = forms.CharField(label= 'Please write your review')
    