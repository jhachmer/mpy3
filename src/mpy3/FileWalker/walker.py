import logging
import os

from mpy3.ID3.ID3V1.id3v1 import ID3V1Tag, ID3V1TagError
from mpy3.Music.album import Album, Track


class MusicTree(object):
    def __init__(self) -> None:
        self.map: dict[str, dict[str, Album]] = {}

    def add_track(self, track: Track) -> None:
        self.map[track.artist][track.album].add_track_to_album(track)

    def add_album(self, album: Album) -> None:
        self.map[album.artist][album.title] = album

    def check_album(self, artist_name: str, album_name: str) -> bool:
        return album_name in self.map[artist_name]

    def check_artist(self, artist_name: str) -> bool:
        return artist_name in self.map


class Walker:
    def __init__(self, path: str) -> None:
        self.path = path

    def walk(self) -> MusicTree:
        tree = MusicTree()
        for root, _, files in os.walk(self.path):
            for file in files:
                # _, filext = os.path.splitext(file)
                # if filext == ".mp3":
                try:
                    track = Track.from_id3v1(ID3V1Tag(os.path.join(root, file)))
                    if not tree.check_artist(track.artist):
                        tree.map[track.artist] = {}
                    if not tree.check_album(track.artist, track.album):
                        tree.add_album(Album(track.album, track.artist, track.year, []))
                    track.track_number = (
                        len(tree.map[track.artist][track.album].tracks) + 1
                    )
                    tree.add_track(track)
                except ID3V1TagError as iderror:
                    logging.error(iderror)
                    continue
                # except Exception as e:
                #     logging.error(f"blubb {e}")
                #     continue

        return tree
