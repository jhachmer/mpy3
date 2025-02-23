from mpy3.FileWalker import Walker

if __name__ == "__main__":
    walker = Walker("E:\\Musik")
    tree = walker.walk()
    for artist, album_names in tree.map.items():
        print(artist)
        for albums in album_names.values():
            print(albums)
