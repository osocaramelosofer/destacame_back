
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/passenger/", include(("passengers.api.urls", "buses"), namespace="api_buses")),
    path("api/routes/", include(("routes.api.urls", "routes"), namespace="api_routes")),
]
