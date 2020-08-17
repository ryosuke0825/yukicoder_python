N = int(input())
ans1 = 0
ans2 = 0
for _ in range(N):
    T, S = input().split()
    t = int(T)
    typing = min(len(S), 12*t//1000)
    ans1 += typing
    ans2 += max(0, len(S)-typing)
print(ans1, ans2)
