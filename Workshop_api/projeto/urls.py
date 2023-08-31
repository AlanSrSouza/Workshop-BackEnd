from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # adicioando todas as urls dentro de todo/
    path('todo/', include('todo.urls'))
]
