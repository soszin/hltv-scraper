from scrapers.Team import Team
import csv

ids = [6665, 5973, 4869, 4608, 6667, 4411, 6211, 9215, 9565, 7533, 6673, 4991, 5995, 8120, 8513, 7801, 8481, 7532, 8297, 8068]

with open('outputs/teams.csv', mode='w') as team:
    team_writer = csv.writer(team, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    team_writer.writerow([
        'Name', 'Country', 'World ranking', 'Flag', 'Logo'
    ])
    for id in ids:
        team = Team(id)
        team_writer.writerow([
            team.get_name(),
            team.get_country(),
            team.get_world_ranking(),
            team.get_country_flag(),
            team.get_team_logo()
        ])
        print(team.get_players())

