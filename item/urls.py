from django.urls import path

from . import views

urlpatterns = [
    path('', views.items, name='items'),
    path('new_item/', views.new_item, name='new_item'),
    path('<int:item_id>/', views.item, name='item'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit_item/', views.edit_item, name='edit_item'),
]