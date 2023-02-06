from django import forms
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, EmailField, PasswordInput
from .models import *

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    subject = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    message = forms.CharField(required=False, widget=forms.Textarea)
    

class MailForm(forms.ModelForm):
    email = EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = CharField(widget=forms.TextInput(attrs={'placeholder': 'subject'}))
    message = CharField(widget=forms.TextInput(attrs={'placeholder': 'Message'}))


    class Meta:
        model = Mail  #
        fields = '__all__'