from rest_framework import serializers

from secure_resource.models import SecureFile, SecureUrl, FileRedirect, UrlRedirect


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureUrl
        fields = ("source_url", "password", "visited")
        read_only_fields = ("password", "visited")


class SecureFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureFile
        fields = ("source_file", "password", "visited")
        read_only_fields = ("password", "visited")


class FileRedirectSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="source.source_file")

    class Meta:
        model = FileRedirect
        fields = ("expires_in", "source")


class UrlRedirectSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source="source.source_url")

    class Meta:
        model = UrlRedirect
        fields = ("expires_in", "source")
