from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from secure_resource.models import SecureFile, SecureUrl


class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = SecureUrl
        fields = ("source_url",)


class FileCreateForm(forms.ModelForm):
    class Meta:
        model = SecureFile
        fields = ("source_file",)


class SecureFileDetailView(LoginRequiredMixin, DetailView):
    model = SecureFile
    template_name = "detail.html"


class SecureUrlDetailView(LoginRequiredMixin, DetailView):
    model = SecureUrl
    template_name = "detail.html"
