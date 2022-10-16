def Combination(n, m):
    b = 1
    c = 1
    for a in range(n, m, -1):
        b *= a
    for a in range(1, n - m + 1):
        c *= a
    d = b // c
    return d

n = eval(input())
sum = 0
if(n % 2):
    for i in range(n // 2 + 1, n):
        j = (i - (n // 2 + 1)) * 2 + 1
        sum += Combination(i, j)
    sum += 1
    print('{}'.format(sum),end='')
else:
    for i in range(n // 2, n):
        j = (i - (n // 2 + 1)) * 2
        sum += Combination(i, j)
    sum += 2
    print('{}'.format(sum),end='')