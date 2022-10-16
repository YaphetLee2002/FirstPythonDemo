a=1
b=2
count=0
n=eval(input())
if n == 1:
    print("1")
elif n == 2:
    print("2")
else:
    first = 1
    double = 2
    
    for i in range (3,n+1):
        count=first+double
        first=double
        double=count
print(count)