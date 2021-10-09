
import string
from random import random
from django.contrib.auth.models import User

from django.db import models
from django.db.models import Model, CharField, DO_NOTHING, ForeignKey, CASCADE


# Create your models here.


class Select(Model):
    title = "nic"


class Game(Model):
    title='nic'


class Room(Model):
    room_number = CharField(max_length=8, unique=True, default='')
    user1 = ForeignKey(User, on_delete=DO_NOTHING, related_name='user_player1', default=None)
    user2 = ForeignKey(User, on_delete=DO_NOTHING, related_name='user_player2', default=None, null=True)




