N = eval(input())
for i in range(5, N+1):
    for a in range(2, i):
        for b in range(a, i):
            for c in range(b, i):
                if(i**3 == a**3 + b**3 + c**3):
                    print('Cube = %d,Tripe = (%d,%d,%d)' %(i, a, b, c))