from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render
import datetime # <=== ZMIANA


from logging import getLogger

from viewer.models import Test

LOGGER = getLogger()

from django.contrib.auth.decorators import login_required # <=NOWE


@login_required # <=NOWE
def generate_demo(request):
    our_get = request.GET.get('name', '')
    return render(
        request, template_name='demo.html',
        context={'our_get': our_get,
                 'list': ['pierwszy', 'drugi', 'trzeci', 'czwarty'],
                 'nasza_data': datetime.datetime.now() # <=== ZMIANA
                 }
    )


class TestView(LoginRequiredMixin, ListView):
    template_name = 'test.html'
    model = Test

