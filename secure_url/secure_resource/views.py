from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponseGone
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from secure_resource.models import SecureFile, SecureUrl, FileRedirect, UrlRedirect
from secure_resource.forms import ConfirmPasswordForm


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


def handle_redirect(model):
    def redirect_view(request, pk):
        obj = get_object_or_404(model, pk=pk)
        now = timezone.now()

        if now >= obj.expires_in:
            return HttpResponseGone("Link has expired.")

        form = ConfirmPasswordForm()
        if request.method == "POST":
            form = ConfirmPasswordForm(request.POST)
            if not form.is_valid():
                return render(request, "redirect.html", {"form": form})
            password = form.cleaned_data["password"]
            if password == obj.get_password():
                return HttpResponseRedirect(obj.get_source_url())
            else:
                form.add_error(None, "Incorect password")

        return render(
            request,
            "redirect.html",
            {
                "form": form,
            },
        )

    return redirect_view


redirect_file_view = handle_redirect(FileRedirect)
redirect_url_view = handle_redirect(UrlRedirect)