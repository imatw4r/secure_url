from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions
from rest_framework.mixins import RetrieveModelMixin

from secure_resource.models import SecureFile, SecureUrl, FileRedirect, UrlRedirect
from secure_resource.api.resources.permissions import IsPasswordCorrect
from secure_resource.api.resources import serializers


class SecureUrlViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SecureUrl.objects.all()
    serializer_class = serializers.UrlSerializer


class SecureFileViewSet(ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SecureFile.objects.all()
    serializer_class = serializers.SecureFileSerializer


class FileRedirectRetrieveModelViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsPasswordCorrect,)
    queryset = FileRedirect.objects.all()
    serializer_class = serializers.FileRedirectSerializer


class UrlRedirectRetrieveModelViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsPasswordCorrect,)
    queryset = UrlRedirect.objects.all()
    serializer_class = serializers.UrlRedirectSerializer
