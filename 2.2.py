list = eval(input())
AppearTimes = {}
for Lable in list:
    if Lable in AppearTimes:
        AppearTimes[Lable] += 1
    else:
        AppearTimes[Lable] = 1
MostCommon = max(AppearTimes, key=lambda x: AppearTimes[x])
print(MostCommon)