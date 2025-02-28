from mpy3.Reader.reader import ByteReader


class ID3V2HeaderError(Exception):
    pass


# TODO: Extract Frames
class ID3V2parser(object):
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self._reader = ByteReader(filename)

    def _check_tag(self, reader: ByteReader) -> bool:
        tag: bytes = reader.read(3)
        return tag == b"ID3"

    def read_tag_header(self, reader: ByteReader):
        if not self._check_tag(reader):
            raise ID3V2HeaderError(
                f"no valid id3v2 header tag found in {self.filename}"
            )
