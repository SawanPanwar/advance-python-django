from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ORS/', include("ORS.urls")),
    path('', include("ORS.urls")),
]
