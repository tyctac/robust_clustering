# start
#encoding=utf-8
N, T = map(int, raw_input().split())
turns = []

for i in range(T):
    a, b, c = map(int, raw_input().split())
    tmp = [a,b,c]
    tmp.sort()
    tp = (tmp[0], tmp[1], tmp[2])
    turns.append(tp)

def get_count(left,t):
    if left == 0 or t>T-1:
        return 0
    if left >= sum(turns[t]):
        return 3 + get_count(left - sum(turns[t]), t+1)
    a = turns[t][0]
    b = turns[t][1]
    c = turns[t][2]
    if left >= b+c:
        s1 = a+b
        s2 = a+c
        s3 = b+c
        m1 = 2 + get_count(left - s1, t+1)
        m2 = 2 + get_count(left - s2, t+1)
        m3 = 2 + get_count(left - s3, t+1)
        max_stage1 =  max(max(m1,m2),m3)
    if left >= a+c:
        # 1 选最大
        s1 = a+c
        # 不选最大
        s2 = a+b
        m1 = 2 + get_count(left - s1, t+1)
        m2 = 2 + get_count(left - s2, t + 1)
        return max(m1,m2)
    if c >= a+b:
        if left >= c:
            # 1 选最大
            s1 = c
            # 不选最大
            s2 = sum(a, b)
            m1 = 1 + get_count(left - s1, t + 1)
            m2 = 2 + get_count(left - s2, t + 1)
            return max(m1,m2)
        elif left >= a+b:
            return 2 + get_count(left-a-b,t+1)
        elif left >= sum(b):
            m1 =  1 + get_count(left - b,t+1)
            m2 = 1 + get_count(left - a, t + 1)
            return max(m1,m2)
        elif left >= a:
            return 1 + get_count(left-a,t+1)
        else:
            return get_count(left, t+1)
    else:
        if left >= a+b:
            m1 = 2+get_count(left-a-b,t+1)
            m2 = 1 + get_count(left - c, t+1)
            return max(m1,m2)
        elif left >= c:
            m1 = 1 + get_count(left - c, t+1)
            m2 = 1 + get_count(left - b, t+1)
            m3 = 1 + get_count(left - a, t+1)
            return max(max(m1,m2),m3)
        elif left >= b:
            m1 = 1 + get_count(left - b, t+1)
            m2 = 1 + get_count(left - a, t+1)
            return max(m1,m2)
        elif left >= a:
            return 1 + get_count(left - a, t+1)
        else:
            return get_count(left, t+1)

print get_count(N,0)
