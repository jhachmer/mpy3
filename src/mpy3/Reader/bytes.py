from typing import Self


class ByteReader(object):
    """ByteReader offer methods to read, skip bytes from a file"""

    def __init__(self, file_path: str):
        self.file = open(file_path, "rb")
        self.file.seek(0, 2)
        self.file_size = self.file.tell()
        self.file.seek(0)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def read(self, n: int) -> bytes:
        """Reads n bytes from file

        Args:
            n (int): Number of bytes to read

        Returns:
            bytes: Returns read bytes
        """
        if self.eof(n):
            raise EOFError("Trying to read beyond end of file")
        return self.file.read(n)

    def seek(self, position: int, whence: int = 0):
        """Sets position of ByteReader

        Args:
            position (int): new position of read pointer
            whence (int, optional):
              os.SEEK_SET or 0 -- start of stream (the default);
                offset should be zero or positive
              os.SEEK_CUR or 1 -- current stream position; offset may be negative
              os.SEEK_END or 2 -- end of stream; offset is usually negative.
              Defaults to 0.
        """
        self.file.seek(position, whence)

    def skip(self, n: int):
        """Skips n amount of bytes after current position

        Args:
            n (int): Number of bytes to skip
        """
        if self.eof(n):
            raise EOFError("Trying to skip beyond end of file")
        self.file.seek(self.file.tell() + n)

    def tell(self) -> int:
        """Returns current position

        Returns:
            int: Current byte position
        """
        return self.file.tell()

    def eof(self, n: int) -> bool:
        return self.tell() + n > self.file_size

    def close(self):
        self.file.close()
