import logging

from mpy3.ID3.ID3V1.v1genres import ID3V1Genre
from mpy3.Reader.reader import ByteReader


class ID3V1TagError(Exception):
    pass


class ID3V1Tag(object):
    def __init__(self, filename: str) -> None:
        _parser: ID3V1Parser = ID3V1Parser(filename)
        data: dict[str, str] = _parser.parse()
        self.title: str = data["title"]
        self.artist: str = data["artist"]
        self.album: str = data["album"]
        self.year: int = int(data["year"])
        self.comment: str = data["comment"]
        self.genre: str = data["genre"]

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Artist: {self.artist}\n"
            f"Album: {self.album}\n"
            f"Year: {self.year}\n"
            f"Comment: {self.comment}\n"
            f"Genre: {self.genre}\n"
        )

    def __repr__(self):
        return str(self)


class ID3V1Parser(object):
    def __init__(self, filename: str):
        self.filename: str = filename
        self._reader: ByteReader = ByteReader(filename)
        self._reader.seek(-128, 2)
        self.data: bytes = self._reader.read(128)
        self.position: int = 0
        self._reader.close()

    def _check_tag(self, tag: bytes) -> bool:
        return tag == b"TAG"

    def read(self, size: int) -> bytes:
        if self.position + size > len(self.data):
            raise EOFError("Trying to read beyond end of data")
        result: bytes = self.data[self.position : self.position + size]
        self.position += size
        return result

    def parse(self) -> dict[str, str]:
        tag: bytes = self.read(3)
        if not self._check_tag(tag):
            raise ID3V1TagError(f"No ID3v1 tag found in file {self.filename}")
        try:
            title: str = self.read(30).decode("utf-8").strip("\x00")
            artist: str = self.read(30).decode("utf-8").strip("\x00")
            album: str = self.read(30).decode("utf-8").strip("\x00")
            year: str = self.read(4).decode("utf-8").strip("\x00")
            year = year if year.isdigit() else "0"
            comment: str = self.read(30).decode("utf-8").strip("\x00").strip()
            genre: int = self.read(1)[0]
            if genre > 191:
                genre = 12
        except UnicodeDecodeError as e:
            logging.error(f"Error decoding ID3v1 tag for file: {self.filename}\n{e}")
            pass

        return {
            "title": title,
            "artist": artist,
            "album": album,
            "year": year,
            "comment": comment,
            "genre": ID3V1Genre(genre).name,
        }
