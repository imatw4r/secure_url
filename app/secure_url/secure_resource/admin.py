from django.contrib import admin

from secure_resource.models import SecureFile, SecureUrl, FileRedirect, UrlRedirect


@admin.register(SecureFile)
class SecureFileAdminModel(admin.ModelAdmin):
    list_display = ["source_file", "created_at", "password"]


@admin.register(SecureUrl)
class SecureUrlAdminModel(admin.ModelAdmin):
    list_display = ["source_url", "created_at", "password"]


@admin.register(FileRedirect)
class FileRedirectAdminModel(admin.ModelAdmin):
    list_display = ["source", "expires_at"]
    list_filter = ["expires_at"]


@admin.register(UrlRedirect)
class UrlRedirectAdminModel(admin.ModelAdmin):
    list_display = ["source", "expires_at"]
    list_filter = ["expires_at"]
