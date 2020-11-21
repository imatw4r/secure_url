from django.contrib import admin

from secure_resource.models import SecureFile, SecureUrl, FileRedirect, UrlRedirect


@admin.register(SecureFile)
class SecureFileAdminModel(admin.ModelAdmin):
    pass


@admin.register(SecureUrl)
class SecureUrlAdminModel(admin.ModelAdmin):
    pass


@admin.register(FileRedirect)
class FileRedirectAdminModel(admin.ModelAdmin):
    pass


@admin.register(UrlRedirect)
class UrlRedirectAdminModel(admin.ModelAdmin):
    pass