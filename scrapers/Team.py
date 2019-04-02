from bs4 import BeautifulSoup
import requests

class Team:
    teamid: None
    responsecontent: ""
    content: ""

    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    def __init__(self, teamid):
        self.teamid = teamid
        self.responsecontent = requests.get("https://www.hltv.org/team/"+str(teamid)+"/astralis", headers=self.hdr)
        self.content = BeautifulSoup(self.responsecontent.content, 'html.parser')

    def get_name(self):
        team_name_container = self.content.select_one(".profile-team-name")
        return team_name_container.get_text().strip()

    def get_country(self):
        country_container = self.content.select_one(".team-country")
        return country_container.get_text().strip()

    def get_world_ranking(self):
        stats_container = self.content.select_one(".profile-team-stats-container")
        return stats_container.div.a.get_text().strip()

    def get_country_flag(self):
        country_container = self.content.select_one(".team-country")
        return country_container.img.get('src')

    def get_team_logo(self):
        logo = self.content.select_one(".teamlogo")
        return logo.get('src')






