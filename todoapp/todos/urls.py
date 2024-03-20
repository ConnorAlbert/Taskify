from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('toggle/todo/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('change_todo_order/<int:todo_id>/<str:direction>/', views.change_todo_order, name='change_todo_order'),
    path('filter_by_priority/', views.filter_by_priority, name='filter_by_priority'),
]0