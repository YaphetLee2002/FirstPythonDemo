import math

def sqrt_binary(num):
    low=0
    high=num
    mid=(low+high)/2
    while math.fabs(
        mid - math.sqrt(num) )>0.0000001:
          if mid<math.pow(num,0.5):
              low=mid
          else:
              high = mid

          mid=(low+high)/2

    return mid

num = float(input())
print(sqrt_binary(num))
tmp = math.sqrt(num)
print(tmp)