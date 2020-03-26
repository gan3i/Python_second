import sys

if __name__ == '__main__':
    n = int(input())
    print(*[x+1 for x in range(n)], sep='', end='\n', file=sys.stdout)
