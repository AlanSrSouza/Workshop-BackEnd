from rest_framework import routers  # importando routers de rest_framerwork
from .views import TodoListViewSet, PessoaViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoListViewSet)
router.register(r'pessoa', PessoaViewSet)
urlpatterns = router.urls  # pra todas
