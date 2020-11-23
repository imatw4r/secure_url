from django.db.models.signals import post_save
from django.dispatch import receiver
from secure_resource.models import (
    SecureElement,
    ElementRedirect,
)


@receiver(post_save, sender=SecureElement)
def create_redirect(sender, instance, created, **kwargs):
    if not created:
        return
    redir_type = ElementRedirect.URL
    if instance.source_file:
        redir_type = ElementRedirect.FILE

    ElementRedirect.objects.create(element=instance, redirect_type=redir_type)
