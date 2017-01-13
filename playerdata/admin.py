
# Register your models here.

from django.contrib import admin

from .models import Player
from .models import PlayerRawStats

admin.site.register(Player)
admin.site.register(PlayerRawStats)