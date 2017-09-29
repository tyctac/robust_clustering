# start
N, T = map(int, raw_input().split())
ai = [-1]
for i in range(N):
    ai.append((int)(raw_input()))

box = [i+1 for i in range(N)]
tmp = [ai[i] for i in box]
start = [0]
start.extend(tmp)
step = (T-1)%N
peri = [[]]
for i in range(1,N+1):
    spos = start[i]
    tp = [start[i]]
    while True:
        if ai[spos] == tp[0]:
            break
        spos = ai[spos]
        tp.append(spos)
    peri.append(tp)

ret = []
for i in range(1,N+1 ):
    step = (T-1)%len(peri[i])
    ret.append(peri[i][step])
for p in ret:
    print p
