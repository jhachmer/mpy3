import pytest

from mpy3.Music.album import Album, Track


def test_track_repr():
    track = Track("Song Title", "Artist Name", "Album Name", 2023, "Genre", 1)
    assert repr(track) == "Artist Name - Song Title"


def test_track_str():
    track = Track("Song Title", "Artist Name", "Album Name", 2023, "Genre", 1)
    assert str(track) == "(1) \t- Song Title"


def test_track_from_id3v1():
    class MockID3v1:
        title = "Song Title"
        artist = "Artist Name"
        album = "Album Name"
        year = 2023
        genre = "Genre"

    id3v1 = MockID3v1()
    track = Track.from_id3v1(id3v1, 1)
    assert track.title == "Song Title"
    assert track.artist == "Artist Name"
    assert track.album == "Album Name"
    assert track.year == 2023
    assert track.genre == "Genre"
    assert track.track_number == 1


def test_album_repr():
    track = Track("Song Title", "Artist Name", "Album Name", 2023, "Genre", 1)
    album = Album("Album Name", "Artist Name", 2023, [track])
    assert repr(album) == "Artist Name - Album Name (2023)"


def test_album_str():
    track = Track("Song Title", "Artist Name", "Album Name", 2023, "Genre", 1)
    album = Album("Album Name", "Artist Name", 2023, [track])
    expected_str = "Artist Name - Album Name (2023)\n(1) \t- Song Title"
    assert str(album) == expected_str


def test_album_getitem():
    track1 = Track("Song Title 1", "Artist Name", "Album Name", 2023, "Genre", 1)
    track2 = Track("Song Title 2", "Artist Name", "Album Name", 2023, "Genre", 2)
    album = Album("Album Name", "Artist Name", 2023, [track1, track2])
    assert album[0] == track1
    assert album[1] == track2


def test_album_len():
    track1 = Track("Song Title 1", "Artist Name", "Album Name", 2023, "Genre", 1)
    track2 = Track("Song Title 2", "Artist Name", "Album Name", 2023, "Genre", 2)
    album = Album("Album Name", "Artist Name", 2023, [track1, track2])
    assert len(album) == 2


def test_add_track_to_album():
    track1 = Track("Song Title 1", "Artist Name", "Album Name", 2023, "Genre", 1)
    track2 = Track("Song Title 2", "Artist Name", "Album Name", 2023, "Genre", 2)
    album = Album("Album Name", "Artist Name", 2023, [track1])
    album.add_track_to_album(track2)
    assert len(album) == 2
    assert album[1] == track2
