from secure_resource.models import SecureFile, SecureUrl
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


class SecureUrlCreateView(LoginRequiredMixin, CreateView):
    template_name = "create.html"
    model = SecureUrl
    fields = ("source_url",)


class SecureFileCreateView(LoginRequiredMixin, CreateView):
    template_name = "create.html"
    model = SecureFile
    fields = ("source_file",)


class SecureFileDetailView(LoginRequiredMixin, DetailView):
    model = SecureFile
    template_name = "detail.html"


class SecureUrlDetailView(LoginRequiredMixin, DetailView):
    model = SecureUrl
    template_name = "detail.html"
