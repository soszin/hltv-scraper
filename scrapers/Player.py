from scrapers.Scraper import Scraper


class Player(Scraper):
    def get_nickname(self):
        nickname_container = self.content.select_one(".playerNickname")
        if nickname_container is None:
            nickname_container = self.content.select_one(".player-nick")
        return nickname_container.get_text(strip=True)

    def get_name(self):
        name_container = self.content.select_one(".playerRealname")
        if name_container is None:
            name_container = self.content.select_one(".player-realname")
        return name_container.get_text(strip=True)

    def get_age(self):
        age_container = self.content.select_one(".playerAge")
        if age_container is None:
            age_container = self.content.select_one(".profile-player-stats-container")
            age = age_container.div.span.get_text(strip=True)
        else:
            age = age_container.span.next_sibling.get_text(strip=True)
        return age

    def get_nationality_flag(self):
        name_container = self.content.select_one(".playerRealname")
        if name_container is None:
            name_container = self.content.select_one(".player-realname")
        return name_container.img.get('src')
