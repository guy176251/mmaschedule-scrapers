from __future__ import annotations

from typing_extensions import TypedDict


class Event(TypedDict):
    name: str
    date: int
    image: str
    fights: list[Fight]
    location: str
    organization: str
    url: str


class Fight(TypedDict):
    weight: str
    fighter_a: Fighter
    fighter_b: Fighter


class Fighter(TypedDict):
    name: str
    image: str
    country: str
