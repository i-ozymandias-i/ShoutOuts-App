from django import forms
from .models import ShoutOut

class ShoutOutForm(forms.ModelForm):
    class Meta:
        model = ShoutOut
        fields = (
            'body',
        )