from django import forms

from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone', 'address', 'city', 'notes')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'phone': forms.TextInput(attrs={'placeholder': '+92 300 0000000'}),
            'address': forms.Textarea(attrs={'placeholder': 'Street address', 'rows': 3}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Order notes (optional)', 'rows': 2}),
        }
