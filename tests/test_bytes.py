import pytest

from mpy3.Reader.bytes import ByteReader


def test_read_within_bounds(tmp_path):
    file_path = tmp_path / "test_file.bin"
    content = b"Hello, World!"
    file_path.write_bytes(content)
    with ByteReader(str(file_path)) as reader:
        assert reader.read(5) == b"Hello"
        assert reader.read(2) == b", "
        assert reader.read(6) == b"World!"


def test_read_beyond_bounds(tmp_path):
    file_path = tmp_path / "test_file.bin"
    content = b"Hello"
    file_path.write_bytes(content)
    with ByteReader(str(file_path)) as reader:
        assert reader.read(5) == b"Hello"
        with pytest.raises(EOFError):
            reader.read(1)


def test_read_exact_bounds(tmp_path):
    file_path = tmp_path / "test_file.bin"
    content = b"Hello"
    file_path.write_bytes(content)
    with ByteReader(str(file_path)) as reader:
        assert reader.read(5) == b"Hello"
        with pytest.raises(EOFError):
            reader.read(1)


def test_seek(tmp_path):
    file_path = tmp_path / "test_file.bin"
    content = b"Hello, World!"
    file_path.write_bytes(content)
    with ByteReader(str(file_path)) as reader:
        reader.seek(7)
        assert reader.read(5) == b"World"


def test_skip(tmp_path):
    file_path = tmp_path / "test_file.bin"
    content = b"Hello, World!"
    file_path.write_bytes(content)
    with ByteReader(str(file_path)) as reader:
        reader.skip(7)
        assert reader.read(5) == b"World"


def test_tell(tmp_path):
    file_path = tmp_path / "test_file.bin"
    content = b"Hello, World!"
    file_path.write_bytes(content)
    with ByteReader(str(file_path)) as reader:
        assert reader.tell() == 0
        reader.read(5)
        assert reader.tell() == 5
        reader.read(2)
        assert reader.tell() == 7
