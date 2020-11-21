import uuid
import datetime

from django.urls import reverse
from django.db import models
from django.utils.crypto import get_random_string

URL_EXPIRATION_TIME = 24 * 60 * 60  # 24h


def generate_password() -> str:
    return get_random_string(length=128)


def get_file_path(instance, filename):
    return f"file/{uuid.uuid4()}/{filename}"


def set_expiration_date():
    return datetime.datetime.utcnow() + datetime.timedelta(seconds=URL_EXPIRATION_TIME)


class SecureUrl(models.Model):
    source_url = models.URLField(max_length=128, null=False)
    password = models.CharField(max_length=128, default=generate_password)

    def __str__(self):
        return self.source_url

    def get_absolute_url(self):
        return reverse("url-detail", kwargs={"pk": self.pk})


class SecureFile(models.Model):
    source_file = models.FileField(upload_to=get_file_path, null=False)
    password = models.CharField(max_length=128, default=generate_password)

    def __str__(self):
        return str(self.source_file)

    def get_absolute_url(self):
        return reverse("file-detail", kwargs={"pk": self.pk})
