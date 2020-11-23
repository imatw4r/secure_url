from django.urls import path, include

from secure_resource.api.routes import router
import secure_resource.views as views


urlpatterns = [
    path("", views.index, name="home"),
    path("file/create", views.SecureFileCreateView.as_view(), name="file-create"),
    path("url/create", views.SecureUrlCreateView.as_view(), name="url-create"),
    path(
        "redirect/element/<int:pk>",
        views.redirect_element_view,
        name="element-redirect",
    ),
    path(
        "element/detail/<int:pk>",
        views.SecureElementDetailView.as_view(),
        name="element-detail",
    ),
    path("api/", include(router.urls)),
]
