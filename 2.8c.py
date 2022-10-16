def SpiralOrder(matrix):
    ans=[]
    try:
        while True:
            ans+=matrix.pop(0)
            for l in matrix:
                ans.append(l.pop())
            ans+=matrix.pop()[::-1]
            for l in matrix[::-1]:
                ans.append(l.pop(0))
    except:
        return ans
matrix = eval(input())
res = SpiralOrder(matrix)
print(res)