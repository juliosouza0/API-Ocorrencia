
from rest_framework.routers import DefaultRouter
from .views import AtendimentoViewSet

router = DefaultRouter()
router.register(r'atendimentos', AtendimentoViewSet)

urlpatterns = router.urls