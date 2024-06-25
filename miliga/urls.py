from django.urls import path, include
from rest_framework import routers
from miliga.views.ligasView import LigasViewSet
from miliga.views.equiposView import EquiposViewSet
from miliga.views.competenciasView import CompetenciasViewSet
from miliga.views.equiposCompetenciasView import EquiposCompetenciasViewSet

router = routers.DefaultRouter()
router.register(r'ligas', LigasViewSet, 'ligas')
router.register(r'equipos', EquiposViewSet, 'equipos')
router.register(r'competencias', CompetenciasViewSet, 'competencias')
router.register(r'equiposcompetencias', EquiposCompetenciasViewSet, 'equiposcompetencias')


urlpatterns = [
    path('', include(router.urls)),
]