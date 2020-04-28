if __name__ == '__main__':
    s = input()
    alpha = False
    num = False
    lw = False
    up = False

    for i in s:
        if i.isalpha() :
            alpha = True
        if i.isdigit() :
            num = True
        if i.islower() :
            lw = True
        if i.isupper() :
            up = True
        if alpha and num and lw and up:
            break


    print(num and alpha)
    print(alpha)
    print(num)
    print(lw)
    print(up)