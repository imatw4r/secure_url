from rest_framework import serializers

from secure_resource.models import ElementRedirect, SecureElement


class SecureUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureElement
        fields = ("source_url", "password")
        read_only_fields = ("password",)


class SecureFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureElement
        fields = ("source_file", "password")
        read_only_fields = ("password",)


class FileRedirectSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="element.source_file")

    class Meta:
        model = ElementRedirect
        fields = ("expires_at", "source")


class UrlRedirectSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="element.source_url")

    class Meta:
        model = ElementRedirect
        fields = ("expires_at", "source")
