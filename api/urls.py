from django.urls import path, include
from rest_framework import routers
from api.views.alumnosView import *
from api.views.telefonosView import *


router = routers.DefaultRouter()
router.register(r'telefonos', TelefonosViewSet, 'telefonos')

urlpatterns = [
    path('', include(router.urls)),
    path('alumnos/', alumnos_list, name='alumnos_list'),
    path('alumnos/<int:pk>/', alumnos_detail, name='alumnos_detail'),
    path('telefonos/telefonosByAlumno/<int:id>/', telefonosByAlumno, name='telefonosByAlumno')
]
# Compare this snippet from api/views.py:
