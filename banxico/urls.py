"""banxico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
from api.views import * 

schema_view = get_schema_view(
   openapi.Info(
      title="Cumplo.com-APIDoc",
      default_version='v1',
      description="Documentación de la api",
      terms_of_service="https://www.cumplo.mx/",
      contact=openapi.Contact(email="ing.blancoross@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('docs/', schema_view.with_ui('swagger', 
            cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', 
            cache_timeout=0), name='schema-redoc'),
    path('api/', include(('api.urls', 'api'))),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)