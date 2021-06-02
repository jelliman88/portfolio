from django.shortcuts import render
import ast
from .models import Team
from .modules import *
from .forms import saveDataForm




def sportsApp(request):
    teams = Team.objects.all()
    return render(request, 'sportsApp.html', {'teams':teams})

def teamDetail(request, team_id):
    if request.POST:
        league_id = request.POST.get('league_id')
        if league_id == 4328:
            pass
        next_5 = Team.refreshData(team_id, league_id)

    #get data from
    data = Team.showData(team_id)
    for i in data:
        league_id = i.league_id
        logo = i.logo.url
        last_updated = i.date_time
        last_5 = ast.literal_eval(i.last_5)
        next_5 = ast.literal_eval(i.next_5)
        standings = ast.literal_eval(i.standings)

    last_5 = Team.shortenDate(last_5)
    next_5 = Team.shortenDate(next_5)
    context = {
        'league_id': league_id,
        'logo': logo,
        'last_5': last_5,
        'next_5': next_5,
        'standings': standings,
        'last_updated' : last_updated
    }
    return render(request, 'teamDetail.html', context)



