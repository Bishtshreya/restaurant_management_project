from django import forms
from .model import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]  # include message field

    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"placeholder": "Enter your message"})
    )  