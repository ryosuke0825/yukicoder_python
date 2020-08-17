W, H, C = input().split()
W = int(W)
H = int(H)

nxt = C
for h in range(H):
    ans = nxt
    for w in range(W-1):
        if ans[-1] == 'B':
            ans += 'W'
        elif ans[-1] == 'W':
            ans += 'B'
    print(ans)

    if nxt == 'B':
        nxt = 'W'
    else:
        nxt = 'B'
