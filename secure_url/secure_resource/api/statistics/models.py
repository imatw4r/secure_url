from django.db import models

from secure_resource.models import FileRedirect, UrlRedirect


class UrlRedirectCount(models.Model):
    redirect = models.ForeignKey(
        UrlRedirect, on_delete=models.CASCADE, related_name="count"
    )
    date = models.DateField(auto_now=True, auto_now_add=True)
