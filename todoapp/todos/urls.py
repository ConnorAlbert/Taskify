from django.urls import path
from . import views

app_name = 'taskify'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.update_taskify, name='update_taskify'),
    path('delete/<int:pk>/', views.delete_taskify, name='delete_taskify'),
    path('toggle/<int:taskify_id>/', views.toggle_taskify, name='toggle_taskify'),
    path('change_order/<int:taskify_id>/<str:direction>/', views.change_taskify_order, name='change_taskify_order'),
    path('filter_by_priority/', views.filter_by_priority, name='filter_by_priority'),
]