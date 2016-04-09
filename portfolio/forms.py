from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        required=True, error_messages={'required': 'Please enter your name'})
    phone = forms.DecimalField(required=False)
    email = forms.EmailField(
        required=True, error_messages={'required': 'Please enter your email id'})
    message = forms.CharField(
        required=True, error_messages={'required': 'Please enter your message'})
