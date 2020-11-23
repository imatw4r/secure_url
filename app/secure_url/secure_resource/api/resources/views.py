from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import permissions
from rest_framework.mixins import RetrieveModelMixin

from secure_resource.models import SecureElement, ElementRedirect
from secure_resource.api.resources.permissions import IsPasswordCorrect
from secure_resource.api.resources import serializers


class SecureUrlViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SecureElement.objects.filter(redirect__redirect_type="URL")
    serializer_class = serializers.SecureUrlSerializer


class SecureFileViewSet(ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = SecureElement.objects.filter(source_url__isnull=True)
    serializer_class = serializers.SecureFileSerializer


class FileRedirectRetrieveModelViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsPasswordCorrect,)
    queryset = ElementRedirect.objects.filter(redirect_type=ElementRedirect.FILE)
    serializer_class = serializers.FileRedirectSerializer


class UrlRedirectRetrieveModelViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsPasswordCorrect,)
    queryset = ElementRedirect.objects.filter(redirect_type=ElementRedirect.URL)
    serializer_class = serializers.UrlRedirectSerializer
