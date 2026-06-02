from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokedex.urls')),  # Rutas de la web normal
    path('api/', include('api.urls')),  # ¡Rutas de tu API de DRF!
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)