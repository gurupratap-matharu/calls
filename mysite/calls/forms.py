from django import forms
from .models import Call

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['duration', 'type']
    
    