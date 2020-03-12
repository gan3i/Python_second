

for i in range(int(input())):
    min_cost,max_cost =sorted(map(int,input().split()))

    first_win = 0
    second_win = 0
    for k in range(int(input())):
        x,y =tuple(map(int,input().split()))
        if x:
            first_win += 1
        if y:
            second_win += 1
    if first_win>second_win:
        print((first_win*min_cost)+(second_win*max_cost))
    else:
        print((first_win*max_cost)+(second_win*min_cost))
