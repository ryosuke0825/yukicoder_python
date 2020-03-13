# https://yukicoder.me/problems/no/29

n = int(input())
A = [0]*10
for _ in range(n):
    tmp = list(map(int, input().split()))
    for t in tmp:
        A[t-1] += 1

ans = 0
for i in range(10):
    ans += A[i]//2
    A[i] = A[i] % 2
ans += sum(A)//4
print(ans)
