from django.urls import path, include
from todos.views import index


urlpatterns = [
    path('', index, name='index'),
    path('taskifys/', include('taskifys.urls', namespace="taskifys")),
]