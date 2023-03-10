import requests
from bs4 import BeautifulSoup
from datetime import date


class Headlines:
    """
    Web-scrapes the Reuters Business home-page for article headlines.
    """

    def __init__(self):
        self.url = "https://www.reuters.com/business"
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, 'html.parser')

    def headlines(self):
        """
        Returns the top 5 headlines of the day.
        """
        headlines = self.soup.select('a[data-testid="Heading''"] span')
        output = []
        for i in range(0, 10, 2):
            output.append(headlines[i].text.strip())
        return output

    def print_news_headlines(self, headlines):
        """
        Prints "Today's News" followed by a bulleted list of headlines.

        Parameters:
            headlines (list): A list of strings representing the headlines to be printed.

        Returns:
            str: A string representing the bulleted list of headlines.
        """
        print("Today's News:")
        bullet_points = '\n'.join([f"• {headline}" for headline in headlines])
        print(bullet_points)
        today = date.today()
        citation = f'Reuters: {today}'
        return citation










