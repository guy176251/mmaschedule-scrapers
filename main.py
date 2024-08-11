from typing_extensions import Callable, TypeAlias
from event import Event
from scrapers import scrape_rizen
from rich import print

Scraper: TypeAlias = Callable[[Event], None]

scrapers: list[Scraper] = [
    scrape_rizen,
]

for scraper in scrapers:
    data: Event = {
        "url": "",
        "name": "",
        "date": 0,  # format is epoch seconds
        "image": "",
        "location": "",
        "organization": "",
        "fights": [],
    }
    scraper(data)
    print(data)
