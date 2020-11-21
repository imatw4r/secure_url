from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions

from secure_resource.models import SecureFile, SecureUrl
from secure_resource.api.resources.serializers import (
    SecureFileSerializer,
    SecureUrlSerializer,
)


class SecureUrlViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SecureUrl.objects.all()
    serializer_class = SecureUrlSerializer


class SecureFileViewSet(ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SecureFile.objects.all()
    serializer_class = SecureFileSerializer
