from django import forms
from website.models import contact , newsletter


class Nameform(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    massage = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):

    def clean_name(self):
        return 'UNKNOWN'
      
    class Meta:
        model = contact
        fields = '__all__'

class newsletterform(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'