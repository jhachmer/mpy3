from mpy3.Reader.bytes import ByteReader


class ID3v2HeaderError(Exception):
    pass


class IDV3UnsupportedVersionError(Exception):
    pass


class ID3V23(object):
    pass


class ID3V24(object):
    pass


class ID3V2Parser(object):
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self._reader = ByteReader(filename)
        self.version, self.revision = self.process_header(self._reader)
        self._reader.close()

    def check_tag(self, tag: bytes) -> bool:
        return tag == b"ID3"

    def process_header(self, reader: ByteReader):
        header: bytes = reader.read(10)
        print(header)
        if not self.check_tag(header[0:3]):
            raise ID3v2HeaderError(
                f"no valid id3v2 header tag found in {self.filename}"
            )
        version: int = header[3]
        revision: int = header[4]
        if version > 4:
            raise IDV3UnsupportedVersionError(
                f"ID3v2.{version}.{revision} is not supported"
            )
        return (version, revision)
