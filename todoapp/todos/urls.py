from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('toggle/todo/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('', views.list_todos, name='list_todos'),
    
    
]