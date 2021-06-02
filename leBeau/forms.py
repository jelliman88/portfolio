from django.forms import ModelForm
from .models import Transaction
from django import forms
from django.forms.widgets import HiddenInput

class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionForm(ModelForm):
   
    class Meta:
        model = Transaction
        exclude = ('created','profit','sold')
        # couldn't add input=date using __init__ 
        widgets = {
            'purchase_date':  DateInput(),
            'selling_date':  DateInput()
        }
        

    # sets attrs 
    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
            # turns required field off on Form
            
            if  'selling' in field_name:
                self.fields[field_name].required = False
            if  field_name == 'tags':
                self.fields[field_name].widget = HiddenInput()
                
            
                


            



            