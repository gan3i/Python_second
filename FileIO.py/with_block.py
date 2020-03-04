
def read_sequence():
        with open("Recaman.txt",mode="rt", encoding= "utf-8") as f:
            return [int(r.strip()) for r in f]

if __name__ == "__main__":
    print(read_sequence())
    