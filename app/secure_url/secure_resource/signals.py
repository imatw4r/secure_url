from django.db.models.signals import post_save
from django.dispatch import receiver
from secure_resource.models import SecureUrl, SecureFile, FileRedirect, UrlRedirect


@receiver(post_save, sender=SecureFile)
def create_file_redirect(sender, instance, created, **kwargs):
    if not created:
        return
    FileRedirect.objects.create(source=instance)


@receiver(post_save, sender=SecureUrl)
def create_url_redirect(sender, instance, created, **kwargs):
    if not created:
        return
    UrlRedirect.objects.create(source=instance)
