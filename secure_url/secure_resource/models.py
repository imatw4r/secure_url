import uuid

from django.db import models
from django.utils.crypto import get_random_string


def generate_password() -> str:
    return get_random_string(length=128)


def get_file_path(instance, filename):
    return f"file/{uuid.uuid4()}/{filename}"


class SecureUrl(models.Model):
    source_url = models.URLField(max_length=128, null=False)
    password = models.CharField(max_length=128, default=generate_password)

    def __str__(self):
        return self.source_url


class SecureFile(models.Model):
    source_file = models.FileField(upload_to=get_file_path, null=False)
    password = models.CharField(max_length=128, default=generate_password)

    def __str__(self):
        return str(self.source_file)
