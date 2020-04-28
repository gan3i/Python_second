

p = [[0,8],[1,7],[2,6],[3,10],[0,2]]

print(sorted(p))
q={}

print(type(q))

for i  in range (len(p)):
    b = p[i][0]
    d = p[i][1]
    if b in q:
        q[b] = q[b]+1
    else:
        q[b] = 1
    if d in q:
        q[d] = q[d]-1
    else:
        q[d] = -1

print(sorted(q))