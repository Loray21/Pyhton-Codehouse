from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import mensajes
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserModel
from django.db.models import Q
from AppEcommerce.views import obtenerAvatar

# Create your views here.


@login_required
def home(request):
    # remplaza import
    User = get_user_model()
    users = User.objects.all()
    chats = {}
    if request.method == 'GET' and 'u' in request.GET:
        chats = mensajes.objects.filter(Q(sender=request.user.id, receiver=request.GET['u']) | Q(
            sender=request.GET['u'], receiver=request.user.id))
        chats = chats.order_by('fecha_envio')
    context = {
        "page": "home",
        "users": users,
        "chats": chats,
        "chat_id": int(request.GET['u'] if request.method == 'GET' and 'u' in request.GET else 0),
        "avatar": obtenerAvatar(request)
    }
    """print(request.GET['u'] if request.method ==
          'GET' and 'u' in request.GET else 0)"""
    return render(request, "appMensajeria/mensajes.html", context)


@login_required
def send_chat(request):
    # print("LLEGA")
    resp = {}
    if request.method == 'POST':
        post = request.POST
        # recupero user receiver y sender
        u_from = UserModel.objects.get(id=post['user_from'])
        u_to = UserModel.objects.get(id=post['user_to'])
        msg = post['mensage']
        insert = mensajes(
            sender=u_from, receiver=u_to, mensaje=msg)
        insert.save()
    return home(request)
