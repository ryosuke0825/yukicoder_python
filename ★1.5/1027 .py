D1, D2 = map(int, input().split())

if D1 == D2/2 or D1 == D2:
    print(4)
elif D2/2 < D1 < D2:
    print(8)
else:
    print(0)
