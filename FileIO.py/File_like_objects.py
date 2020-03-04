

def words_per_line(f):
    return [len(line.split()) for line in f.readlines()]


def read_file():
    with open("wasteland.txt",mode= "rt",encoding="utf=8") as flo:
        print(words_per_line(flo))
        print(type(flo))


def get_text():

    from urllib.request import urlopen
    with urlopen("https://sixty-north.com/c/t.txt") as flo:
        print(words_per_line(flo))
        print(flo)
        print(type(flo))





if __name__ == "__main__":
    read_file()
    get_text()