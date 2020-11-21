from django.contrib import admin

from user_agent.models import UserAgent


@admin.register(UserAgent)
class UserAgentAdminModel(admin.ModelAdmin):
    list_display = ["user", "user_agent"]
