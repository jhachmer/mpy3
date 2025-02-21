class ByteReader(object):
    def __init__(self, file_path: str):
        self.file = open(file_path, "rb")

    def read(self, size: int) -> bytes:
        return self.file.read(size)

    def seek(self, position: int, whence: int = 0):
        self.file.seek(position, whence)

    def skip(self, size: int):
        self.file.seek(self.file.tell() + size)

    def tell(self) -> int:
        return self.file.tell()

    def eof(self) -> bool:
        current_pos = self.file.tell()
        self.file.seek(0, 2)
        end_pos = self.file.tell()
        self.file.seek(current_pos)
        return current_pos >= end_pos

    def close(self):
        self.file.close()
