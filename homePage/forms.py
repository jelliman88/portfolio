from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Name*', 'required': 'True', 'name':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email*', 'required': 'True'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message*', 'required': 'True'}))