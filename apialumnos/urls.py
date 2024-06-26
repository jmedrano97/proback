
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic.base import RedirectView

# Schema view para Alumnos
alumnos_schema_view = get_schema_view(
   openapi.Info(
      title="Alumnos API",
      default_version='v1',
      description="Prueba de API para alumnos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jaime08medrano@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   patterns=[path('colegio/', include('api.urls'))],
)

# Schema view para Mi Liga
miliga_schema_view = get_schema_view(
   openapi.Info(
      title="Mi Liga API",
      default_version='v1',
      description="Prueba de API para mi liga",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jaime08medrano@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   patterns=[path('miliga/', include('miliga.urls'))],
)

urlpatterns = [
    path('', RedirectView.as_view(url='docs/', permanent=True)),
    path('admin/', admin.site.urls),
    path('colegio/', include('api.urls')),
    path('miliga/', include('miliga.urls')),
    path('docs/miliga', miliga_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/alumnos', alumnos_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
