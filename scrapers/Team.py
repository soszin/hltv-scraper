from scrapers.Scraper import Scraper
import re

class Team(Scraper):
    def __init__(self, url):
        super().__init__(url)

    def get_name(self):
        team_name_container = self.content.select_one(".profile-team-name")
        return team_name_container.get_text().strip()

    def get_country(self):
        country_container = self.content.select_one(".team-country")
        return country_container.get_text().strip()

    def get_world_ranking(self):
        stats_container = self.content.select_one(".profile-team-stats-container")
        word_ranking = stats_container.div.a

        if word_ranking:
            return stats_container.div.a.get_text().strip()
        else:
            return '#0'

    def get_country_flag(self):
        country_container = self.content.select_one(".team-country")
        return country_container.img.get('src')

    def get_team_logo(self):
        logo = self.content.select_one(".teamlogo")
        return logo.get('src')

    def get_players(self):
        players = self.content.select(".bodyshot-team a")
        ids = []
        for player in players:
            url = player.get('href')
            player_id = re.findall("\/player\/(.*)\/.*", url)
            ids.append(int(player_id[0]))
        return ids





