# Class to get odds info from DK

import requests
from bs4 import BeautifulSoup
class DK:
    def __init__(self):
        pass

    @staticmethod
    def get_nba_events():
        """ Gets the games displayed on draftkings.
        Can use the links here appended to draftkings.com to get to the game odds screen
        Returns: A list of links in the form /event/team1-%40-team2/eventID
        """
        url = 'https://sportsbook.draftkings.com/leagues/basketball/nba'

        response = requests.get(url)
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        events = soup.find_all('a', class_='event-cell-link')
        links = []

        for event in events:
            link = event.get('href')
            if link and (link not in links):
                links.append(link)
        return links
    
    @staticmethod
    def get_game_odds(link):
        """
        Gets the odds for the specific link provided
        """