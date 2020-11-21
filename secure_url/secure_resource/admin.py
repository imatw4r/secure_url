from django.contrib import admin
from secure_resource.models import SecureFile, SecureUrl


@admin.register(SecureFile)
class SecureFileAdminModel(admin.ModelAdmin):
    pass


@admin.register(SecureUrl)
class SecureUrlAdminModel(admin.ModelAdmin):
    pass
