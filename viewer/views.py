import cgi
import random
import string

import requests as requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import datetime  # <=== ZMIANA

from logging import getLogger

from viewer.models import Select, Room

LOGGER = getLogger()

from django.contrib.auth.decorators import login_required  # <=NOWE


@login_required  # <=NOWE
def generate_demo(request):
    our_get = request.GET.get('name', '')
    return render(
        request, template_name='demo.html',
        context={'our_get': our_get,
                 'list': ['pierwszy', 'drugi', 'trzeci', 'czwarty'],
                 'nasza_data': datetime.datetime.now()  # <=== ZMIANA
                 }
    )


class SelectView(LoginRequiredMixin, ListView):
    template_name = 'select.html'
    model = Select



class GameCreateView(LoginRequiredMixin, View):
    def get(self, request):
        code = "".join(random.choices(string.ascii_uppercase, k=6))
        Room.objects.create(room_number=code, user1=request.user)
        return HttpResponseRedirect(reverse('game', kwargs={'game_code': code}))


class GameJoinView(LoginRequiredMixin, View):
    context = {}
    def post(self, request):
        if request.method == 'POST':
            code = request.POST.get('room_code')
            return HttpResponseRedirect(reverse('game', kwargs={'game_code': code}))


class GameView(LoginRequiredMixin, View):
    def get(self, request, game_code):
        if request.method == 'POST':
            game_code = request.POST.get('game_code')
        room = Room.objects.filter(room_number=game_code).first()
        if request.user.id == room.user1.id:
            pass
        elif room.user2 == None:
            room.user2 = request.user
        elif room.user2.id == request.user.id:
            pass
        else:
            raise ('Nie możesz dołączyć, bo w pokoju jest już dwoje graczy!')
        return render(request, template_name='game.html',
                      context={})
