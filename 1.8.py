def is_Prime(n):  ##判断是否为素数，返回布尔值
    while n <= 1:  ##输入值的异常处理
        print("输入的数值错误，请重新输入！")
        n = int(input("请输入一个数值："))
    if n == 2:  ##对于2做特殊处理
        return True
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return False
            else:
                return True


a = int(input("请输入一个数值："))
print("%s" % is_Prime(int(a)))

j = 0
m = 2
while True:
    if prime(m):
        j += 1
        if j == 1001:
            print(m)
            break
    m += 1
