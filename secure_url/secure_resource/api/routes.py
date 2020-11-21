from rest_framework.routers import SimpleRouter

import secure_resource.api.resources.views as views

router = SimpleRouter()
router.register("resources/url", views.SecureUrlViewSet)
router.register("resources/file", views.SecureFileViewSet)
router.register(
    "resources/file_redirect",
    views.FileRedirectRetrieveModelViewSet,
)
router.register("resources/url_redirect", views.UrlRedirectRetrieveModelViewSet)
