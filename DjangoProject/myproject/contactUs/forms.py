from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50,required=True)
    contact_email = forms.EmailField(max_length=50,required=True)
    Mnumber = forms.IntegerField(max_length = 10,required=True) 
    Subject = forms.CharField(max_length=200,required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )