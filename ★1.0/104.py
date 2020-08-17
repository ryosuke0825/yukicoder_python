S = list(input())

left = 1
for s in S:
    left *= 2
    if s == 'R':
        left += 1
print(left)
