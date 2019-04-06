from scrapers.Scraper import Scraper


class Team(Scraper):
    def __init__(self, teamid):
        self.teamid = teamid
        super().__init__()

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

    def get_players(self):
        players = self.content.select(".bodyshot-team a")
        urls = []
        for player in players:
            urls.append(player.get('href'))
        return urls

    def setUrl(self):
        return "https://www.hltv.org/team/"+str(self.teamid)+"/astralis"





