from typing_extensions import Callable, TypeAlias
from event import Event
from scrapers import scrape_rizen
from rich import print

Scraper: TypeAlias = Callable[[list[Event]], None]

scrapers: list[Scraper] = [
    scrape_rizen,
]

for scraper in scrapers:
    data: list[Event] = []
    scraper(data)
    print(data)
