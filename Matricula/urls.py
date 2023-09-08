from rest_framework import routers
from .api import AlumnoViewSet

router = routers.DefaultRouter()
router.register('api/alumnos',AlumnoViewSet,'Matricula')

urlpatterns = router.urls
