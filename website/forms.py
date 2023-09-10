from django import forms
from captcha.fields import CaptchaField
from website.models import contact , newsletter

class Nameform(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    massage = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
   
    class Meta:
        model = contact
        fields = '__all__'

    def clean_name(self):
        return 'UNKNOWN'
      

class newsletterform(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'