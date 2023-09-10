from django import forms
from captcha.fields import CaptchaField
from blog.models import comment

class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['post' , 'name' , 'email' , 'subject', 'massage', ]