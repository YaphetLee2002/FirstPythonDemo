MoneyWithUnit = input()
if MoneyWithUnit[0:3] in ["RMB"]:
    money = (eval(MoneyWithUnit[3:])/6.78)
    print("USD{:.2f}".format(money))
elif MoneyWithUnit[0:1] in ["￥"]:
    money = (eval(MoneyWithUnit[1:])/6.78)
    print("${:.2f}".format(money))
elif MoneyWithUnit[0:3] in ["USD"]:
    money = 6.78*eval(MoneyWithUnit[3:])
    print("RMB{:.2f}".format(money))
else:
    money = 6.78*eval(MoneyWithUnit[1:])
    print("￥{:.2f}".format(money))