from rest_framework.routers import SimpleRouter

from secure_resource.api.resources.views import SecureFileViewSet, SecureUrlViewSet

router = SimpleRouter()
router.register("resources/url", SecureUrlViewSet)
router.register("resources/file", SecureFileViewSet)
