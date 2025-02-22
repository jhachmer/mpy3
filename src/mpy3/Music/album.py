from dataclasses import dataclass
from datetime import datetime


@dataclass
class Track(object):
    title: str
    artist: str
    album: str
    year: datetime
    genre: str
    track_number: int


@dataclass
class Album(object):
    title: str
    artist: str
    year: datetime
    genre: str
    tracks: list[Track]
    total_tracks: int
