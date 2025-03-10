import pytest

from mpy3.ID3.id3v2 import ID3v2HeaderError, ID3V2Parser, IDV3UnsupportedVersionError


@pytest.fixture
def valid_versions():
    return [3, 4]


@pytest.fixture
def mp3_file_mock(tmp_path, contents: bytes):
    file_path = tmp_path / "test.mp3"
    file_path.write_bytes(contents)
    return file_path


@pytest.mark.parametrize(
    "contents",
    [
        b"ID3\x03\x00\x00\x00\x00\x00\x00\x00\x00",
        b"ID3\x04\x00\x00\x00\x00\x00\x00\x00\x00",
    ],
)
def test_process_header_valid_version(mp3_file_mock, valid_versions):
    id3 = ID3V2Parser(mp3_file_mock)
    assert id3.version in valid_versions


@pytest.mark.parametrize(
    "contents",
    [
        b"ID3\x05\x00\x00\x00\x00\x00\x00\x00\x00",
        b"ID3\x06\x00\x00\x00\x00\x00\x00\x00\x00",
    ],
)
def test_process_header_invalid_version(mp3_file_mock):
    with pytest.raises(IDV3UnsupportedVersionError):
        id3 = ID3V2Parser(mp3_file_mock)
        id3.process_header(id3._reader)


@pytest.mark.parametrize(
    "contents",
    [
        b"XYZ\x03\x00\x00\x00\x00\x00\x00\x00\x00",
        b"XYZ\x04\x00\x00\x00\x00\x00\x00\x00\x00",
    ],
)
def test_process_header_invalid_tag(mp3_file_mock):
    with pytest.raises(ID3v2HeaderError):
        id3 = ID3V2Parser(mp3_file_mock)
        id3.process_header(id3._reader)


@pytest.mark.parametrize(
    "contents",
    [
        b"ID3\x03\x00\x00\x00\x00\x00\x00\x00\x00",
    ],
)
def test_check_tag(mp3_file_mock):
    id3 = ID3V2Parser(mp3_file_mock)
    assert id3.check_tag(b"ID3") is True
    assert id3.check_tag(b"XYZ") is False
