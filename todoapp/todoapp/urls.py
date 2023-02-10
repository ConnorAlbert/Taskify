from django.urls import path, include
from todos.views import index


urlpatterns = [
    path('', index, name='index'),
    path('todos/', include('todos.urls', namespace="todos")),
    path('__debug__/', include('debug_toolbar.urls')),
]