from django.forms import ModelForm
from .models import Team


class saveDataForm(ModelForm):
    
    class Meta:
        model = Team
        fields = ('next_5','last_5', 'standings')







    
