import io

# f = io.BytesIO(b"some initial binary data: \x00\x01")
f = open("13 - Would.mp3", mode="rb")

print(f.read(3))
f.close()

with open("13 - Would.mp3", mode="rb") as f:
    f.seek(-128, 2)
    id3v1 = f.read(128)
    print(f"{id3v1.decode("utf-8")}\n")


class ByteReader(object):
    def __init__(self, data: bytes, pos: int = 0):
        self.data: bytes = data
        self.position: int = pos

    def read(self, size: int) -> bytes:
        if self.position + size > len(self.data):
            raise EOFError("Attempting to read beyond end of data")
        result: bytes = self.data[self.position : self.position + size]
        self.position += size
        return result
