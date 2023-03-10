# Headline scraper for the business homepage of Reuters
from scraper import Headlines

today = Headlines()
output = today.headlines()
print(today.print_news_headlines(output))




