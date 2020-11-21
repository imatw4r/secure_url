from rest_framework import serializers

from secure_resource.models import SecureFile, SecureUrl, FileRedirect, UrlRedirect


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureUrl
        fields = ("source_url", "password")
        read_only_fields = ("password",)


class SecureFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureFile
        fields = ("source_file", "password")
        read_only_fields = ("password",)


class FileRedirectSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="source.source_file")

    class Meta:
        model = FileRedirect
        fields = ("expires_in", "source")


class UrlRedirectSerializer(serializers.ModelSerializer):
    source = serializers.Field(source="source.source_url")

    class Meta:
        model = UrlRedirect
        fields = ("expires_in", "source")
