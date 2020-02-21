from scrapers.Team import Team
from scrapers.Player import Player
import csv
import pika
import json
import os

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channelTeams = connection.channel()
channelPlayers = connection.channel()
channelTeams.queue_declare(queue='teams')
channelPlayers.queue_declare(queue='players')

# team_ids = [6665, 5973, 4869, 4608, 6667, 4411, 6211, 9215, 9565, 7533, 6673, 4991, 5995, 8120, 8513, 7801, 8481, 7532, 8297, 8068]
team_ids = [6665]
# team_ids = [6667]

os.remove('outputs/teams.csv')
# os.remove('outputs/players.csv')

with open('outputs/teams.csv', mode='w') as team:
    team_writer = csv.writer(team, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    team_writer.writerow([
        'Name', 'Country', 'World ranking', 'Flag', 'Logo'
    ])
    for team_id in team_ids:
        team = Team("https://www.hltv.org/team/"+str(team_id)+"/astralis")
        teamData = {
            "external_id": team_id,
            "name": team.get_name(),
            "country": team.get_country(),
            "ranking": team.get_world_ranking(),
            "flag_url": team.get_country_flag(),
            "logo_url": team.get_team_logo()
        }
        team_writer.writerow(teamData)
        team_players_ids = team.get_players()
        channelTeams.basic_publish(exchange='', routing_key='teams', body=json.dumps(teamData))


with open('outputs/players.csv', mode='w', encoding='utf8') as player:
    player_writer = csv.writer(player, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    player_writer.writerow([
        'Real name', 'Nickname', 'Age', 'Nationality'
    ])
    for player_id in team_players_ids:
        player = Player("https://www.hltv.org/player/"+str(player_id)+"/Xyp9x")
        playerData = {
            "external_id": player_id,
            "name": player.get_name(),
            "nickname": player.get_nickname(),
            "age": player.get_age(),
            "flag_url": player.get_nationality_flag()
        }
        player_writer.writerow(playerData)
        channelPlayers.basic_publish(exchange='', routing_key='players', body=json.dumps(playerData))


connection.close()
