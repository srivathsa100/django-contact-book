from django import forms
from .models import Contact

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['FirstName', 'LastName', 'Email', 'ContactNumber', 'picture']
