from django.urls import path

import secure_resource.views as views
from secure_resource.api.routes import router


urlpatterns = [
    path("file/create", views.SecureFileCreateView.as_view(), name="file-create"),
    path(
        "file/detail/<int:pk>", views.SecureFileDetailView.as_view(), name="file-detail"
    ),
    path("url/create", views.SecureUrlCreateView.as_view(), name="url-create"),
    path("url/detail/<int:pk>", views.SecureUrlDetailView.as_view(), name="url-detail"),
]

urlpatterns += router.urls
