M = eval(input())
N = eval(input())
up = 1
down = 1
for i in range(N, M + N - 1):
    up *= i
for j in range(1, M):
    down *= j
print(up // down)