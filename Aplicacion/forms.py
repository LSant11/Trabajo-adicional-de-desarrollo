from django import forms
from .models import Ferreteria,Usuario

class ferreform (forms.ModelForm):
    class  Meta:
        model =  Ferreteria
        fields = '__all__'
        
class Usuariform (forms.ModelForm):
    class  Meta:
        model =  Usuario
        fields = '__all__'