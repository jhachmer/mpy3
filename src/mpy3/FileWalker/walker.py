import logging
import os

from mpy3.IDV3.ID3V1.id3v1 import ID3V1Tag, ID3V1TagError
from mpy3.Music.album import Album, Track


class Walker:
    def __init__(self, path):
        self.path = path

    def walk(self):
        # albums = []
        prev_dir = None
        for root, dirs, files in os.walk(self.path):
            if prev_dir is None and dirs == []:
                prev_dir = root

            if prev_dir != root:
                tracks = []
                for file in files:
                    _, filext = os.path.splitext(file)
                    if filext == ".mp3":
                        try:
                            track = Track.from_id3v1(
                                ID3V1Tag(os.path.join(root, file)), len(tracks) + 1
                            )
                            tracks.append(track)
                        except ID3V1TagError as iderror:
                            logging.info(iderror)
                            continue
                        except Exception as e:
                            logging.error(e)
                            continue
                if len(tracks) > 0:
                    album = Album(
                        tracks[0].album,
                        tracks[0].artist,
                        tracks[0].year,
                        tracks,
                        len(tracks),
                    )
                    # albums.append(album)
                    yield album
        # return albums
