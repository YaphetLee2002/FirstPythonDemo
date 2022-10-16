Income = eval(input())
IncomeBeforeTax = Income - 5000
if IncomeBeforeTax < 0:
    IncomeBeforeTax = 0


def Correct_Income(Income):
    if Income < 0:
        return False
    else:
        return True


def Tax_Rate(IncomeBeforeTax):
    if IncomeBeforeTax <= 3000:
        return 0.03
    elif IncomeBeforeTax <= 12000:
        return 0.1
    elif IncomeBeforeTax <= 25000:
        return 0.2
    elif IncomeBeforeTax <= 35000:
        return 0.25
    elif IncomeBeforeTax <= 55000:
        return 0.3
    elif IncomeBeforeTax <= 80000:
        return 0.35
    else:
        return 0.45


def main():
    if Correct_Income(Income):
        IncomeAfterTax = IncomeBeforeTax * Tax_Rate(IncomeBeforeTax)
        print('%.1f' % IncomeAfterTax)
    else:
        print("请输入正数！")


main()
