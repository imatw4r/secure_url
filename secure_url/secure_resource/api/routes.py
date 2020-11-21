from rest_framework.routers import SimpleRouter
from secure_resource.api.views import SecureFileViewSet, SecureUrlViewSet

router = SimpleRouter()
router.register("api/url", SecureUrlViewSet)
router.register("api/file", SecureFileViewSet)
