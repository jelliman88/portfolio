from django.db import models
import requests
from .modules import *
import ast
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta, date
from django.contrib.humanize.templatetags.humanize import ordinal
from theTone.settings import SPORTSDB_KEY

class Team(models.Model):
    league_id = models.IntegerField()
    team_id = models.IntegerField()
    logo = models.ImageField(upload_to='sportsApp/logos')
    last_5 = models.TextField(default='[]')
    next_5 = models.TextField(default='[]')
    standings = models.TextField(default='[]')
    date_time = models.DateTimeField(blank=True)

    def showData(team_id):

        queryset = Team.objects.filter(team_id=team_id)

        return queryset

    def refreshData(team_id, league_id):
        # urls
        last_5_url = f"https://www.thesportsdb.com/api/v1/json/{SPORTSDB_KEY}/eventslast.php?id={team_id}"
        next_5_url = f"https://www.thesportsdb.com/api/v1/json/{SPORTSDB_KEY}/eventsnext.php?id={team_id}"
        standings_url = f"https://www.thesportsdb.com/api/v1/json/{SPORTSDB_KEY}/lookuptable.php?l=4328&s=2020-2021"

        # api call
        last_5_response = requests.get(last_5_url)
        next_5_response = requests.get(next_5_url)

        info = []


        if league_id == '4328': #EPL
            standings_response = requests.get(standings_url)
            standings = standings_response.json()
            info.append(standings)


        # convert from json
        last_5 = last_5_response.json()
        next_5 = next_5_response.json()

        info.extend([last_5, next_5])

        for response in info:

            # last_5
            if 'results' in response.keys():
                last_5_list = []
                the_filter = last_filter

            # next_5
            if 'events' in response.keys():
                next_5_list = []
                the_filter = next_filter

            # epl table
            if 'table' in response.keys():
                standings_list = []
                the_filter = epl_table_filter


            # extract
            for key, value in response.items():
                if value is not None:
                    for game in value:
                        game_info = {}
                        for subkey, subvalue in game.items():
                            if subkey in the_filter:
                                # filter to get team nickname
                                if 'Team' in subkey:
                                    if subvalue == 'Boston Red Sox':
                                        subvalue = 'BOS'
                                    if subvalue == 'Chicago White Sox':
                                        subvalue = 'CWS'
                                    split_string = subvalue.split(" ")
                                    subvalue = split_string[-1]
                                    # nickname check
                                    if subvalue in nicknames:
                                        subvalue = nicknames.get(subvalue)

                                # filter to shorten time
                                elif 'Time' in subkey:
                                    start_time = datetime.strptime(subvalue, '%H:%M:%S').time()
                                    # round the houses as python wont allow + datetime.time and timedelta
                                    dt = datetime.combine(date.today(), start_time) + timedelta(hours=2)
                                    adjusted_dt = str(dt.time())
                                    split_string = adjusted_dt.split(":")
                                    subvalue = f"{split_string[0]}:{split_string[1]}"

                                game_info[subkey] = subvalue



                        # append to corresponding list
                        if 'strStatus' in the_filter:
                            next_5_list.append(game_info)
                        elif 'win' in the_filter:
                            standings_list.append(game_info)
                        else:
                            last_5_list.append(game_info)



        # save to database
        obj = get_object_or_404(Team, team_id=team_id)
        obj.last_5 = last_5_list
        obj.next_5 = next_5_list
        obj.date_time = datetime.now() + timedelta(hours=2)
        if league_id == '4328':
            obj.standings = standings_list

        obj.save(update_fields=['last_5','next_5', 'standings', 'date_time'])



    def shortenDate(game_list):
        for game in game_list:
            date_string = game.get('dateEvent')
            day =  datetime.strptime(date_string, '%Y-%m-%d').strftime('%A')
            date = ordinal(int(f"{date_string[8]}{date_string[9]}"))
            game['dateEvent'] = f'{day} {date}'
        return game_list