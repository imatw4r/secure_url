from django.apps import AppConfig


class SecureResourceConfig(AppConfig):
    name = "secure_resource"

    def ready(self):
        import secure_resource.signals  # noqa
