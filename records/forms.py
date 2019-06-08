from django import forms
from records.models import *     

class ArtistForm(forms.ModelForm):  
  class Meta:  
    model = Artist
    fields = "__all__"  