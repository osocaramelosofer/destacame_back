
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/passenger/", include(("passengers.api.urls", "buses"), namespace="api_buses")),
    path("api/routes/", include(("routes.api.urls", "routes"), namespace="api_routes")),
    path("api/buses/", include(("buses.api.urls", "buses"), namespace="api_buses")),
    path("api/journeys/", include(("journeys.api.urls", "journeys"), namespace="api_journeys")),

    path('buses/', include(('buses.urls', 'buses2'), namespace='buses2')),
]
