from django.urls import path
from .views import chatbot_page, chat_view

urlpatterns = [
    path("", chatbot_page, name="chat_page"),
    path("chat/", chat_view, name="chat_api"),
]
