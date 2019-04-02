from scrapers.Team import Team
from datetime import datetime

ids = [6665, 5973, 4869, 4608, 6667, 4411, 6211, 9215, 9565, 7533, 6673, 4991, 5995, 8120, 8513, 7801, 8481, 7532, 8297, 8068]

for id in ids:
    team = Team(id)
    print("-------------------------------")
    print("Name: " + team.get_name())
    print("Country: " + team.get_country())
    print("World ranking: " + team.get_world_ranking())
    print("Country flag: " + team.get_country_flag())
    print("Logo: " + team.get_team_logo())