from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("code/", include("codes.urls")),
    path("", home, name="home"),
    path("login/", auth, name="auth"),
    path("varify/", varify_view, name="varify"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
