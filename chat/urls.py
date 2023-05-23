from django.urls import path

from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:id>/', views.chat_detail, name='chat_detail'),
    path('chat/<int:item_id>', views.new_chat, name='chat'),
]