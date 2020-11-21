from django.urls import include, path
from secure_resource.api.routes import router

urlpatterns = []

urlpatterns += router.urls
