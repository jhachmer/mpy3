import os
from mpy3.ID3V1.id3v1 import ID3V1Tag, ID3V1TagError


class Walker:
    def __init__(self, path):
        self.path = path

    def walk(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                _, filext = os.path.splitext(file)
                if filext == ".mp3":
                    try:
                        yield ID3V1Tag(os.path.join(root, file))
                    except ID3V1TagError as iderror:
                        print(iderror)
                        continue
                    except Exception as e:
                        print(e)
            # for dir in dirs:
            #     yield os.path.join(root, dir)
