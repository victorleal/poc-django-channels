from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="chat-index"),
    path("<str:room_name>/", views.room_view, name="chat_room"),
    path("<str:room_name>/announce", views.room_announce, name="chat_announcement"),
]
