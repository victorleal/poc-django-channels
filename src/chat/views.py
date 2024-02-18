from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from chat.models import Room


def index_view(request):
    return render(
        request,
        "chat/index.html",
        {
            "rooms": Room.objects.all(),
        },
    )


def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, "chat/room.html", {"room": chat_room})


def room_announce(request, room_name):
    channel_layer = get_channel_layer()
    print(room_name)
    async_to_sync(channel_layer.group_send)(
        f"chat_{room_name}",
        {
            "type": "chat_message",
            "message": "ANNOUNCEMENT TO EVERYONE HAHAHAHA",
        },
    )

    return render(request, "chat/announcement.html")
