from scrapers.Team import Team
from scrapers.Player import Player
import csv

team_ids = [6665, 5973, 4869, 4608, 6667, 4411, 6211, 9215, 9565, 7533, 6673, 4991, 5995, 8120, 8513, 7801, 8481, 7532, 8297, 8068]
# team_ids = [6667]
team_players_urls = []

with open('outputs/teams.csv', mode='w') as team:
    team_writer = csv.writer(team, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    team_writer.writerow([
        'Name', 'Country', 'World ranking', 'Flag', 'Logo'
    ])
    for team_id in team_ids:
        team = Team("https://www.hltv.org/team/"+str(team_id)+"/astralis")
        team_writer.writerow([
            team.get_name(),
            team.get_country(),
            team.get_world_ranking(),
            team.get_country_flag(),
            team.get_team_logo()
        ])
        team_players_urls.append(team.get_players())


with open('outputs/players.csv', mode='w', encoding='utf8') as team:
    player_writer = csv.writer(team, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    player_writer.writerow([
        'Real name', 'Nickname', 'Age', 'Nationality'
    ])
    for players_url in team_players_urls:
        for player_url in players_url:
            player = Player("https://www.hltv.org" + player_url)
            player_writer.writerow([
                player.get_name(),
                player.get_nickname(),
                player.get_age(),
                player.get_nationality_flag()
            ])



