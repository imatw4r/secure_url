import uuid
import datetime

from django.urls import reverse
from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.conf import settings


def generate_password() -> str:
    return get_random_string(length=128)


def get_file_path(instance, filename):
    return f"file/{uuid.uuid4()}/{filename}"


def set_expiration_date():
    return timezone.now() + datetime.timedelta(seconds=settings.URL_EXPIRATION_TIME)


class SecureElement(models.Model):
    source_url = models.URLField(max_length=128, null=True)
    source_file = models.FileField(upload_to=get_file_path, null=True)
    password = models.CharField(max_length=128, default=generate_password)
    created_at = models.DateField(auto_now_add=True, editable=True)

    def get_source_url(self):
        if self.source_url:
            return self.source_url
        return self.source_file.url

    def get_password(self):
        return self.password

    def get_absolute_url(self):
        return reverse("element-detail", kwargs={"pk": self.pk})

    def increase_count(self):
        self.visited += 1
        self.save()


class ElementRedirect(models.Model):
    FILE = "FILE"
    URL = "URL"
    TYPES = [
        (FILE, "File"),
        (URL, "Url"),
    ]
    element = models.OneToOneField(
        SecureElement, on_delete=models.CASCADE, related_name="redirect"
    )
    expires_at = models.DateTimeField(default=set_expiration_date, null=False)
    redirect_type = models.CharField(max_length=5, choices=TYPES, null=False)
    visited = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True, editable=True)

    def get_absolute_url(self):
        return reverse("element-redirect", kwargs={"pk": self.pk})

    def get_password(self):
        return self.element.password

    def get_source_url(self):
        return self.element.get_source_url()

    def increase_count(self):
        self.visited += 1
        self.save()