from django import forms
from .models import Feedback
from .model import Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        error_messages={
            'invalid': 'Please enter a valid email address.',
            'required': 'Email is required.'
        }
    )

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

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Your feedback"}),
        }
        labels = {
            "name": "Name",
            "message": "Feedback",
        }