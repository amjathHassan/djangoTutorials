from django import forms
from django.forms import ModelForm
from .models import ModelFormDB

class SignUpForm(forms.Form):
    first_name = forms.CharField(label= "First Name ", widget= forms.TextInput(attrs={'class': 'fname'}))
    last_name = forms.CharField(label= "Last Name ", widget= forms.TextInput(attrs={'class': 'lname'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'email'}))
    review = forms.CharField(label="Enter additional information here",
                            widget= forms.Textarea(attrs={
                                'class': 'newform',
                                'rows': '5',
                                'cols' : '50',
                            }))


class FormModelFormDB(ModelForm):
    class Meta:
        model = ModelFormDB
        fields = "__all__"
        # fields = ["first_name", "last_name"]
