from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import auction
from auction import views
# from auction.views import List_View

from home import settings

# app_name = "shop"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("auction.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
