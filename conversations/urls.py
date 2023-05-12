from django.urls import path

from . import views

urlpatterns = [
   
    path('chat/<int:house_pk>', views.new_conversation, name='chat'),
    path('/inboxs', views.inbox_conversations, name='inbox_messages'),
]