import collections

N = int(input())
L = list(map(int, input().split()))
c = collections.Counter(L)

cnt = 0
ans = 0
for i in range(1, 7):
    if i in c:
        if c[i] >= cnt:
            ans = i
            cnt = c[i]
print(ans)
