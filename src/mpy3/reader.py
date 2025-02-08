from typing import Literal

# f = io.BytesIO(b"some initial binary data: \x00\x01")
f = open("13 - Would.mp3", mode="rb")

print(f.read(3))
f.close()

with open("13 - Would.mp3", mode="rb") as f:
    f.seek(-128, 2)
    id3v1 = f.read(128)
    print(f"{id3v1.decode('utf-8')}\n")


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
