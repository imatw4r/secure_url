import uuid
import datetime

from django.urls import reverse
from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone

URL_EXPIRATION_TIME = 24 * 60 * 60  # 24h


def generate_password() -> str:
    return get_random_string(length=128)


def get_file_path(instance, filename):
    return f"file/{uuid.uuid4()}/{filename}"


def set_expiration_date():
    return timezone.now() + datetime.timedelta(seconds=URL_EXPIRATION_TIME)


class SecureUrl(models.Model):
    source_url = models.URLField(max_length=128, null=False)
    password = models.CharField(max_length=128, default=generate_password)
    visited = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.source_url

    def get_absolute_url(self):
        return reverse("url-detail", kwargs={"pk": self.pk})

    def increase_count(self):
        self.visited += 1
        self.save()


class SecureFile(models.Model):
    source_file = models.FileField(upload_to=get_file_path, null=False)
    password = models.CharField(max_length=128, default=generate_password)
    visited = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True, editable=True)

    def __str__(self):
        return str(self.source_file)

    def get_absolute_url(self):
        return reverse("file-detail", kwargs={"pk": self.pk})

    def increase_count(self):
        self.visited += 1
        self.save()


class FileRedirect(models.Model):
    source = models.OneToOneField(
        SecureFile, on_delete=models.CASCADE, related_name="redirect"
    )
    expires_at = models.DateTimeField(default=set_expiration_date, null=False)

    def get_absolute_url(self):
        return reverse("file-redirect", kwargs={"pk": self.pk})

    def get_source_url(self):
        return self.source.source_file.url

    def get_password(self):
        return self.source.password

    def __str__(self):
        return str(self.source)


class UrlRedirect(models.Model):
    source = models.OneToOneField(
        SecureUrl, on_delete=models.CASCADE, related_name="redirect"
    )
    expires_at = models.DateTimeField(default=set_expiration_date, null=False)

    def get_absolute_url(self):
        return reverse("url-redirect", kwargs={"pk": self.pk})

    def get_source_url(self):
        return self.source.source_url

    def get_password(self):
        return self.source.password

    def __str__(self):
        return str(self.source)