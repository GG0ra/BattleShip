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

from viewer.models import Select, Room, Layout

LOGGER = getLogger()

from django.contrib.auth.decorators import login_required  # <=NOWE


@login_required  # <=NOWE
def generate_board(request):
    our_get = request.GET.get('name', '')
    return render(
        request, template_name='board.html',
        context={'our_get': our_get,
                 'columns': ['A', 'B', 'C', 'D', 'E'],
                 'rows': ['1', '2', '3', '4', '5']
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
        if request.method == "POST":
            game_code = request.POST.get('game_code')
        room = Room.objects.filter(room_number=game_code).first()
        if request.user.id == room.user1.id:
            pass
        elif room.user2 == None:
            room.user2 = request.user
            room.save()
        elif room.user2.id == request.user.id:
            pass
        else:
            raise ('Nie możesz dołączyć, bo w pokoju jest już dwoje graczy!')
        return render(request, template_name='game.html',
                      context={'columns': ['A', 'B', 'C', 'D', 'E'],
                               'rows': ['1', '2', '3', '4', '5'],
                               'game_code': game_code})


class LayoutView(LoginRequiredMixin, View):
    context = {}

    def post(self, request, game_code):
        if request.method == 'POST':
            id_list = request.POST.getlist('choices')
            Layout.objects.create(room_number=game_code, user=request.user, coor0=id_list[0], coor1=id_list[1],
                                  coor2=id_list[2],
                                  coor3=id_list[3], coor4=id_list[4], coor5=id_list[5])
            return HttpResponseRedirect(reverse('shooting', kwargs={'game_code': game_code}))


class ShootingView(LoginRequiredMixin, View):
    def get(self, request, game_code):
        if request.method == "POST":
            game_code = request.POST.get('game_code')
        return render(request, template_name='shooting.html',
                      context={'columns': ['A', 'B', 'C', 'D', 'E'],
                               'rows': ['1', '2', '3', '4', '5'],
                               'game_code': game_code})


class ResultView(LoginRequiredMixin, View):
    context = {}

    def post(self, request, game_code):
        if request.method == 'POST':
            opp_layout = Layout.objects.filter(room_number=game_code).exclude(user=request.user).first()
            shot_list = request.POST.getlist('shots')
            points = 0
            for i in shot_list:
                if i == opp_layout.coor0:
                    points += 1
                if i == opp_layout.coor1:
                    points += 1
                if i == opp_layout.coor2:
                    points += 1
                if i == opp_layout.coor3:
                    points += 1
                if i == opp_layout.coor4:
                    points += 1
                if i == opp_layout.coor5:
                    points += 1
            user_layout = Layout.objects.filter(room_number=game_code).filter(user=request.user).first()
            user_layout.points=points
            user_layout.save()
            return render(request, template_name='result.html',
                          context={'game_code': game_code,
                                   'points': points})
