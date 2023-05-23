from django.urls import path

from . import views

urlpatterns = [
    path('new_item/', views.new_item, name='new_item'),
    path('<int:item_id>/', views.item, name='item'),
]