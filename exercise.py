count = 1
for i in range(153, 408):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i and count <= 3:
        print('{},'.format(i), end='')
        count+=1
    elif a**3 + b**3 + c**3 == i and count == 4:
        print('{}' .format(i), end='')