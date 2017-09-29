## start
N, k = map(int, raw_input().split())
parent = [-1 for i in range(N+1)]
for i in range(1,N+1):
    li, ri = map(int, raw_input().split())
    if li != 0:
        parent[li] = (i, 0)
    if ri != 0:
        parent[ri] = (i, 1)

retstr = ''
while True:
    tp = parent[k]
    if tp == -1:
        break
    if tp[1] == 0:
        retstr = 'L' + retstr
    elif tp[1] == 1:
        retstr = 'R' + retstr
    k = tp[0]

print retstr
