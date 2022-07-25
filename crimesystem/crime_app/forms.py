
# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import *
 
# create a ModelForm
class casesform(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = cases
        fields = "__all__"
        # exclude = ['title']