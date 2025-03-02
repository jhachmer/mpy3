from dataclasses import dataclass


@dataclass
class Track:
    title: str
    artist: str
    album: str
    year: int
    genre: str
    track_number: int

    def __repr__(self) -> str:
        return f"{self.artist} - {self.title}"

    def __str__(self) -> str:
        return f"({self.track_number}) \t- {self.title}"

    @classmethod
    def from_id3v1(cls, id3v1, track_number=0):
        return cls(
            id3v1.title,
            id3v1.artist,
            id3v1.album,
            id3v1.year,
            id3v1.genre,
            track_number,
        )


@dataclass
class Album:
    title: str
    artist: str
    year: int
    tracks: list[Track]

    def __repr__(self) -> str:
        return f"{self.artist} - {self.title} ({self.year})"

    def __str__(self) -> str:
        return (
            f"{self.artist} - {self.title} ({self.year})\n"
            f"{'\n'.join([str(track) for track in self.tracks])}"
        )

    def __getitem__(self, pos: int) -> Track:
        return self.tracks[pos]

    def __len__(self) -> int:
        return len(self.tracks)

    def add_track_to_album(self, track: Track) -> None:
        self.tracks.append(track)
        self.total_tracks = len(self.tracks) + 1
