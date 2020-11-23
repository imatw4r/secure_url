from django.contrib import admin

from secure_resource.models import ElementRedirect, SecureElement


@admin.register(SecureElement)
class SecureElementAdminModel(admin.ModelAdmin):
    list_display = ["source_file", "source_url", "created_at", "password"]
    list_filter = ["source_file", "source_url"]


@admin.register(ElementRedirect)
class ElementRedirectAdminModel(admin.ModelAdmin):
    list_display = [
        "redirect_type",
        "visited",
        "created_at",
    ]
    list_filter = [
        "redirect_type",
    ]
