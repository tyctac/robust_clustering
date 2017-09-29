# staret
# start
N, T = map(int, raw_input().split())
a = []
b = []
for i in range(N):
    tmp = (int)(raw_input())
    a.append((i,tmp))
for j in range(T):
    b.append((int)(raw_input()))
b.sort()
a.sort(lambda x,y: x[1] - y[1])
f = {}
ret = [-1 for i in range(N)]
max = 1
fmax = 1
for x in a:
    ai = x[1]
    tp = 1
    rn = fmax
    tp = fmax
    if ai == max:
        tp = fmax
        ret[x[0]] = tp
        continue
    while ai > max:
        rn = rn +1
        while rn in b:
            rn +=1
        tp += 1
    max = tp
    fmax = tp
    ret.append(tp)
print ret
