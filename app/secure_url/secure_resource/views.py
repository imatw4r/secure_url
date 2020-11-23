from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponseGone
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from secure_resource.models import (
    SecureElement,
    ElementRedirect,
)
from secure_resource.forms import (
    ConfirmPasswordForm,
)


class SecureUrlCreateView(LoginRequiredMixin, CreateView):
    model = SecureElement
    template_name = "create.html"
    fields = ("source_url",)


class SecureFileCreateView(LoginRequiredMixin, CreateView):
    model = SecureElement
    template_name = "create.html"
    fields = ("source_file",)


class SecureElementDetailView(LoginRequiredMixin, DetailView):
    model = SecureElement
    template_name = "detail.html"


def index(request):
    return render(request, "home.html")


def redirect_element_view(request, pk):
    obj = get_object_or_404(ElementRedirect, pk=pk)
    now = timezone.now()

    if now >= obj.expires_at:
        return HttpResponseGone("Link has expired.")

    form = ConfirmPasswordForm()
    if request.method == "POST":
        form = ConfirmPasswordForm(request.POST)
        if not form.is_valid():
            return render(request, "redirect.html", {"form": form})
        password = form.cleaned_data["password"]
        if password == obj.get_password():
            # @TODO: This should be done in an asynch way in a task
            #        with queue
            obj.increase_count()
            return HttpResponseRedirect(obj.get_source_url())
        else:
            form.add_error(None, "Incorect password")

    return render(
        request,
        "redirect.html",
        {"form": form},
    )
