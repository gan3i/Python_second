import sys
from itertools import count,islice


def sequense():
    """Generate Recaman's Sequence"""
    seen = set ()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a =  c


def write_sequence(filename, num):
    """write recaman's series to text file"""
    f = open(filename, mode="wt",encoding="utf-8")
    f.writelines(f"{r}\n" for r in islice(sequense(),num+1))
    # f.writelines(f"sdf\n")
    f.close()


def read_sequence(filename):
    try:
        f = open(filename, mode="rt", encoding= "utf-8")
        series = []
        return [int(r.strip()) for r in f]
        # for line in f :
        #         a = int(line.strip())
        #         series.append(a)
        #         print(a)
        #f.close()
    finally:
        print("finally")
        f.close()
    return series




if __name__ == "__main__":
    write_sequence("Recaman.txt",8)
    read_sequence("Recaman.txt")