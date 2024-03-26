from .models import Subscriber
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Your Phone Number'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']