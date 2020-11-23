from django import forms
from secure_resource.models import SecureElement


class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())


class SecureFileCreateForm(forms.ModelForm):
    class Meta:
        fields = ["source_file"]
        model = SecureElement


class SecureUrlCreateForm(forms.ModelForm):
    class Meta:
        fields = ["source_url"]
        model = SecureElement
