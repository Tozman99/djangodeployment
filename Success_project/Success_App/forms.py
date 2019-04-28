from django import forms 
from Success_App.models import User


class User_form(forms.ModelForm):
    class Meta:
        model= User 
        fields = '__all__'
