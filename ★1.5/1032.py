import collections

N, M = map(int, input().split())
L = list(map(int, input().split()))

c = collections.Counter(L)

for i in range(1, M+1):
    if i in c:
        print(i, c[i])
    else:
        print(i, 0)
