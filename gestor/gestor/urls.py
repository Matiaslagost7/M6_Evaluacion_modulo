from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # URLs de autenticación en el nivel raíz
    path('', include('app_login.urls')),
    
    # URLs Públicas - Sin autenticación requerida
    path('', include('tareas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
