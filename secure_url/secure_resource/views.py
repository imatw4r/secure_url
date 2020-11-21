from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from secure_resource.models import SecureFile, SecureUrl, FileRedirect, UrlRedirect


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


class RedirectElementDetailView(DetailView):
    template_name = "detail.html"
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        redirect = self.get_object().redirect.first()
        context["redirect"] = redirect
        return context


class RedirectUrlDetailView(RedirectElementDetailView):
    model = UrlRedirect


class RedirectFileDetailView(RedirectElementDetailView):
    model = FileRedirect
