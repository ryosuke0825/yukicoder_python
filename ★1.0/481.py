B = list(map(int, input().split()))
for i in range(1, 11):
    if not(i in B):
        print(i)
        break
