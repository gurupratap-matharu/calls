from django import forms

from calls.models import Call


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ["duration", "category"]
