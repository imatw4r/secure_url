from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from secure_resource.api.routes import router
import secure_resource.views as views


urlpatterns = [
    path("", views.index, name="home"),
    path("file/create", views.SecureFileCreateView.as_view(), name="file-create"),
    path(
        "file/detail/<int:pk>", views.SecureFileDetailView.as_view(), name="file-detail"
    ),
    path(
        "file/redirect/<int:pk>",
        views.redirect_file_view,
        name="file-redirect",
    ),
    path("url/create", views.SecureUrlCreateView.as_view(), name="url-create"),
    path("url/detail/<int:pk>", views.SecureUrlDetailView.as_view(), name="url-detail"),
    path(
        "url/redirect/<int:pk>",
        views.redirect_url_view,
        name="url-redirect",
    ),
    path("api/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)