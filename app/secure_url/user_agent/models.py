from django.db import models
from django.contrib.auth import get_user_model


class UserAgent(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="user_agent"
    )
    user_agent = models.TextField(verbose_name="User Agent", null=True)
