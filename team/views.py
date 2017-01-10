from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import generic

from team import services


class TeamPage(generic.TemplateView):
    def get(self,request):
        team_list = services.get_player_data()
        return render(request, 'team/team_list.html', {'data': team_list})
