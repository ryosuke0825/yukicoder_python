N = input()

for _ in range(100):
    n_list = list(N)
    if len(n_list) == 1:
        break
    a = 0
    for n in n_list:
        a += int(n)
    N = str(a)
print(''.join(n_list))
