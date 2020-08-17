N = int(input())
ONE_DAY = 60*24
ans = 0
for _ in range(N):
    hm = input().split()
    hm1 = hm[0].split(':')
    hm1_sum = int(hm1[0])*60+int(hm1[1])
    hm2 = hm[1].split(':')
    hm2_sum = int(hm2[0])*60+int(hm2[1])

    if hm1_sum < hm2_sum:
        ans += hm2_sum-hm1_sum
    elif hm1_sum > hm2_sum:
        ans += (ONE_DAY-hm1_sum)+hm2_sum

print(ans)
