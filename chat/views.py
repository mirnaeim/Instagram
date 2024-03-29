from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


@login_required(login_url='/api-auth/login/')
def index2(request):
    return render(request, "chat/index2.html", {"sender_username": request.user.username})


def direct(request, room_name):
    return render(request, "chat/direct.html", {"room_name": room_name})

#
# def room(request, room_name):
#     return render(request, "chat/room.html", {"room_name": room_name})
