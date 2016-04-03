from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label="Your Name:", required=True)
    email = forms.EmailField(label="Email ID:", required=True)
    message = forms.CharField(label="Message:", widget=forms.Textarea, required=True)
