from secure_resource.models import SecureFile, SecureUrl
from rest_framework.serializers import ModelSerializer


class SecureUrlSerializer(ModelSerializer):
    class Meta:
        model = SecureUrl
        fields = ("source_url", "password")
        read_only_fields = ("password",)


class SecureFileSerializer(ModelSerializer):
    class Meta:
        model = SecureFile
        fields = ("source_file", "password")
        read_only_fields = ("password",)
